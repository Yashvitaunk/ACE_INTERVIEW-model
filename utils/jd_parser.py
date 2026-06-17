def read_jd(jd_path):

    with open(jd_path, "r", encoding="utf-8") as file:
        jd_text = file.read()

    return jd_text