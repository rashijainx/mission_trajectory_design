import yaml

class Planet:
    def __init__(self, name, **properties):
        self.name = name
        for key, value in properties.items():
            setattr(self, key, value)

    @classmethod
    def from_yaml(cls, yaml_file, planet_name):
        with open(yaml_file, "r") as f:
            data = yaml.safe_load(f)

        planets_dict = data.get("planets", {})
        planet_data = planets_dict.get(planet_name)
        if planet_data is None:
            raise ValueError(f"Planet '{planet_name}' not found in {yaml_file}")

        return cls(planet_name, **planet_data)

    # handy helper
    def scale_vec_by_radius(self, vec_in_radii):
        return tuple(self.radius_km * x for x in vec_in_radii)