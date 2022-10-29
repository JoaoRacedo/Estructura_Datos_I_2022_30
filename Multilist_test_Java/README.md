## Folder Structure

The workspace contains two folders by default, where:

- `src`: the folder to maintain sources
- `lib`: the folder to maintain dependencies
- `doc`: the folder to src documentation (work in progress)

to create the documentation use:

```console
path/to/proyect/Multilist_test_java:~$ javadoc -d chose_path/to_save_doc/ path_to_script/LL_Empleados.java
```

to learn more about javadoc:
[tutorialspoint example](https://www.tutorialspoint.com/java/java_documentation.htm#:~:text=What%20is%20Javadoc%3F,are%20Java%20multi%2Dline%20comments.)
[javadoc oracle tutorial](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html)

Meanwhile, the compiled output files will be generated in the `bin` folder by default.

> If you want to customize the folder structure, open `.vscode/settings.json` and update the related settings there.

## Dependency Management

The `JAVA PROJECTS` view allows you to manage your dependencies. More details can be found [here](https://github.com/microsoft/vscode-java-dependency#manage-dependencies).
