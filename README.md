# Notes

- Currently the container lacks the "debug redistributables" so cannot run a debug build.

# Dependency Analysis

- Use [Dependencies](https://github.com/lucasg/Dependencies)
    - *Don't use:* [DependencyWalker](http://dependencywalker.com/) (`depends.exe`)
- Possible workflow:
    - Inspect with `DependenciesGui.exe` outside the container.
    - Use: `$ where XXXXX.dll` inside the container.