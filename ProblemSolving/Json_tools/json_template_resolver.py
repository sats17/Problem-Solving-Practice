


if __name__ == "__main__":
    resolver = JsonTemplateResolver("test_json.json",
                                    {"update_me_1": "resolved first", "update_me_2": "resolved second"})
    result = resolver.generate()
    print(type(result))
    json_str = json.dumps(result, indent=4)
    print(type(json_str))
    print(json_str)