# unturned-analyse
Assembly-CSharp.dll version: 3.24.7.0

A platform for analyzing Unturned's core code and simplifying plugin development. It integrates DocFX for generating and hosting documentation on GitHub Pages.

You can download [Assembly-CSharp.xml](https://github.com/Sonus-Mutationis/unturned-analyse/blob/main/assembly/Assembly-CSharp.xml) and [Assembly-CSharp.dll](https://github.com/Sonus-Mutationis/unturned-analyse/blob/main/assembly/Assembly-CSharp.dll), then use [dnSpy](https://github.com/dnSpy/dnSpy)/[ILSpy](https://github.com/icsharpcode/ILSpy)/[dotPeek](https://www.jetbrains.com/decompiler/) to analyze the DLL file. This will help you take your understanding beyond Nelson's documentation to the next level!


## For Documentation Contributors

You can navigate to the `xml-documentation` directory in this repository and create files named `<namespace>.<class-name>.xml`. We implement a "one class, one XML file" system, which allows for better management of custom documentation files without getting confused by automatically generated XML documentation.

The XML merging tool is being developed in Python and is currently a work in progress.

Like this:

```xml
<!-- TestNamespace.TestClass.xml -->
<?xml version="1.0" encoding="utf-8"?>
<doc>
  <member name="T:TestNamespace.TestClass">
    <summary>This is a test class.</summary>
    <remarks>This class is used for testing purposes.</remarks>
    <example>Here's an example of how to use this class:</example>
  </member>
  <member name="M:TestNamespace.TestClass.TestMethod">
    <summary>This is a test method.</summary>
    <remarks>This method is used for testing purposes.</remarks>
    <example>Here's an example of how to use this method:</example>
  </member>
  <!-- Add more members as needed -->
</doc>
```

The `summary` tag is used to provide a brief description of the class, while the `remarks` tag is used to provide more detailed information. The `example` tag is used to provide an example of how to use the class.


## Useful Documentation Links

[Documentation comments](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/) - Learn about XML documentation comments in C#, including their purpose and basic syntax.

[Recommended XML tags for C# documentation comments](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/recommended-tags) - Explore Microsoft's comprehensive guide to recommended XML tags for documenting your C# code.