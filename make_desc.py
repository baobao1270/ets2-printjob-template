import os
import toml
import shutil
import datetime
import xml.etree.ElementTree as et

TAILERS_LIST_MAPPING = {
    "cn": {
        "type": {"C": "侧帘干货车", "D": "干货车", "I": "隔热车", "F": "冷藏车", "T": "食品罐车"},
        "length": {"136": "全挂", "78": "半挂", "2": ""},
        "feature": {"B": "B型双挂", "M": "带活动底板", "S": "侧门", "C": "镀铬", "N": ""},   
    }, "en": {
        "type": {"C": "Curtain", "D": "Dry Van", "I": "Insulated", "F": "Refrigerated", "T": "Food Tank"},
        "length": {"136": "136", "78": "78", "2": ""},
        "feature": {"B": " B-Double", "M": " Moving Floor", "S": " Side", "C": " Chrome", "N": ""}
    }
}

def tailers_list(code_list, sii=False):
    lines = [];
    for code in code_list:
        code_parts = [code[0], code[1:-1], code[-1]]
        code_en = "{type}{feature} {length}".format(
            type=TAILERS_LIST_MAPPING["en"]["type"][code_parts[0]],
            length=TAILERS_LIST_MAPPING["en"]["length"][code_parts[1]],
            feature=TAILERS_LIST_MAPPING["en"]["feature"][code_parts[2]],
        )
        code_cn = "{en}（{length}{feature}{type}）".format(
            en=code_en,
            type=TAILERS_LIST_MAPPING["cn"]["type"][code_parts[0]],
            length=TAILERS_LIST_MAPPING["cn"]["length"][code_parts[1]],
            feature=TAILERS_LIST_MAPPING["cn"]["feature"][code_parts[2]],
        )
        lines.append(code_cn)
    if sii:
        return "\n".join(lines)
    lines_ubb = ["    [*]{}".format(i) for i in lines]
    return "[list]\n{}\n[/list]".format("\n".join(lines_ubb))

def ubb2sii(text):
    UBB_REPLACES = {
        "h1": "orange",
        "url": "blue",
        "b": "red",
        "code": "green",
    }
    import re
    for ubb_tag, scs_tag in UBB_REPLACES.items():
        flags = re.IGNORECASE if (ubb_tag != "code") else re.DOTALL | re.IGNORECASE
        regex = r"\[{tag}\](.*?)\[/{tag}\]".format(tag=ubb_tag)
        text = re.sub(
            regex,
            lambda m: "[{scs}]{content}[normal]".format(scs=scs_tag, content=m.group(1)),
            text,
            flags=flags
        )
    text = text.replace("。", ". ")
    text = text.replace("，", ", ")
    text = text.replace("：", ": ")
    text = text.replace("（", " (")
    text = text.replace("）", ") ")
    return text

def make_readme(config):
    license_text = open("LICENSE", encoding="utf-8").read()
    license_hint = "启用本模组, 意味着您同意本模组的许可证. 您可以在 Steam Workshop 或模组发布页获取许可证副本."
    readme_ubb   = open("README_STEAM.txt", encoding="utf-8").read()
    readme_sii = ubb2sii(readme_ubb)
    readme_ubb = readme_ubb.format(
        name=config["name"], version=config["version"], author=config["author"],
        year=datetime.date.today().year, license=license_text, models=tailers_list(config["tailers"])
    )
    readme_sii = readme_sii.format(
        name=config["name"], version=config["version"], author=config["author"],
        year=datetime.date.today().year, license=license_hint, models=tailers_list(config["tailers"], True)
    )
    return readme_ubb, readme_sii

def update_xml(config, readme_sii):
    with open("mod.ms2", encoding="utf-8") as f:
        template_xml = f.read()
    project = et.fromstring(template_xml)

    for node in project.find("ScsModManifest").find("Variables"):
        if node.find("Name").text == "display_name":
            node.find("Value").text = config["name"]
            continue
        if node.find("Name").text == "author":
            node.find("Value").text = config["author"]
            continue
        if node.find("Name").text == "package_version":
            node.find("Value").text = config["version"]
            continue
        if node.find("Name").text == "description":
            node.find("Value").text = readme_sii
            continue
        if node.find("Name").text == "icon":
            node.find("Value").text = os.path.abspath(os.path.join(os.path.dirname(__file__), "icons/mod_icon.jpg"))
            continue
    
    et.ElementTree(project).write("mod.ms2")

def main():
    config = toml.load("config.toml")
    if not os.path.exists("mod.ms2"):
        shutil.copy("mod_template.xml", "mod.ms2")
    readme_ubb, readme_sii = make_readme(config)
    with open("READM_STEAM_OUT.txt", "w+", encoding="utf-8") as f: f.write(readme_ubb)
    update_xml(config, readme_sii)

if __name__ == "__main__":
    main()
