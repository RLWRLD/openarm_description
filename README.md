# Robot Description files for OpenArm

This package contains description files to generate OpenArm URDFs (Universal Robot Description Files). See [documentation](https://docs.openarm.dev/software/description) for details.

## How to use
For non-ROS2 users,
```bash
xacro urdf/robot/v10.urdf.xacro ee_type:=rh56f1 standalone:=true > openarm_rh56f1.urdf
```

If you are familiar with ROS2, skipping `standalone` argument will modify urdf to search properties(meshs, ...) based on package directory:
```bash
xacro urdf/robot/v10.urdf.xacro ee_type:=rh56f1 > openarm_rh56f1.urdf
```

## Related links

- 📚 Read the [documentation](https://docs.openarm.dev/software/description)
- 💬 Join the community on [Discord](https://discord.gg/FsZaZ4z3We)
- 📬 Contact us through <openarm@enactic.ai>

## License

[Apache License 2.0](LICENSE.txt)

Copyright 2025 Enactic, Inc.

## Code of Conduct

All participation in the OpenArm project is governed by our
[Code of Conduct](CODE_OF_CONDUCT.md).
