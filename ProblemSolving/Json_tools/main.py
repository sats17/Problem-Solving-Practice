from ProblemSolving.Json_tools.json_template_resolver import JsonTemplateResolver


if __name__ == "__main__":
    resolver = JsonTemplateResolver("test_json.json",
                                    {"update_me_1": "resolved first", "update_me_2": "resolved second"})
    resolver.generate()