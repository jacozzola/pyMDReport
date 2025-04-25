# pyMDReport
pyMDReport is a Python package made to automatically create .md reports  
It's purpose is to easily create well-organized good-looking .md files. A good usage example could be to create a .md report after running tests on your script

## Table of contents
- [How to install](#how-to-install)   
- [Documentation](#documentation)
    - [pyMDComponent](#pymdcomponent)
        - [pyMDComponent.GetAnchor](#pyMDComponent-GetAnchor)
        - [pyMDComponent.Md](#pyMDComponent-Md)
        - [pyMDComponent.BaseMd](#pyMDComponent-BaseMd)
    - [ComponentType](#componenttype)
    - [Group](#group)
        - [Group.Add](#Group-Add)
        - [Group.Update](#Group-Update)
        - [Group.Get](#Group-Get)
    - [Text](#text)
        - [Text.Fill](#Text-Fill)
    - [Heading](#heading)
    - [Quote](#quote)
    - [Link](#link)

## How To Install
pyMDReport can be installed via *pip* through  

`pip install pyMDReport`

## Documentation

### pyMDComponent
Every component in pyMDReport is a child class of **pyMDComponent**.     
pyMDComponents are objects that can be converted in Markdown (md) format.       
A pyMDComponent has: 
- an *identifier* ( if not given will use `uuid.uuid4()` )
- possibly a *parent* ( a **Group**, which is also a pyMDComponent )    
- a *type* ( consts from ComponentType class)
```python
class pyMDComponent:
    _identifier: str
    _parent: Group | None
    _type: ComponentType
    def __init__( self,
            parent: Group | None = None,
            identifier: str | None = None,
        )
    def GetAnchor( self ) -> str
    def BaseMd( self ) -> str
    def Md( self ) -> str
```
if *parent* is specified, the component is automatically added to the parent's *components* dict    
Every pyMDComponent has these 3 methods:
```python
class pyMDComponent:
    def GetAnchor( self ) -> str
    def BaseMd( self ) -> str
    def Md( self ) -> str
```

<a id="pyMDComponent-GetAnchor"></a>

- **GetAnchor**    
    ```python
    def GetAnchor(self) -> list[str]
    ``` 
    The GetAnchor method is responsible of returning the id of the element's anchor.
    Every component has a unique anchor by default, but it's not active until the *GetAnchor* method is called. 
<br/>

<a id="pyMDComponent-Md"></a>

- **Md**    
    ```python
    def Md( self ) -> str
    ``` 
    The Md method defines how the component is converted into MD format.  
    This method is overwritten in subclasses based on how each component converts into MD format.
<br/>

<a id="pyMDComponent-BaseMd"></a>

- **BaseMd**   
    ```python
    def BaseMd( self ) -> str
    ``` 
    The BaseMd method is responsible of calculating and returning the MD strings preceding the component's MD string (for example, the anchor's MD string if the anchor is active).   
    Each component's *Md* method should first call the *BaseMd* method and then add the component's MD representation.
<br/>

### ComponentType
```python
class ComponentType:
    none = 0x00
    pymdcomponent = 0x01

    group = 0x100
    report = 0x101

    text = 0x200
    heading = 0x201
    quote = 0x202
    link = 0x203
    image = 0x204
```
**ComponentType** contains constants that are unique for each component type.

### Group
```python
class Group(pyMDComponent):
    _components : dict[str, pyMDComponent]
    def __init__( self, 
            parent : Group | None = None, 
            identifier : str | None = None,
        )
    def Add( self,
            component: pyMDComponent,
        ) -> None
    def Update( self,
            componentIdentifier: str,
            component: pyMDComponent,  
        ) -> None
    def Get( self, identifier: str | list[str] ) -> pyMDComponent
```
Child class of [pyMDComponent](#pymdcomponent).     
A **Group** is a component that "contains" other components.       
Components are associated to their *identifier* in Group.components          
```python
Group.components = {
    "example" : pyMDComponent,
}
``` 
Every Group has these methods:
```python
class Group (pyMDComponent):
    def Add( self,
            component: pyMDComponent,
        ) -> None
    def Update( self,
            componentIdentifier: str,
            component: pyMDComponent,  
        ) -> None
    def Get( self, identifier: str | list[str] ) -> pyMDComponent
```
<a id="Group-Add"></a>
- **Add**   
    ```python
    def Add( self,
            component: pyMDComponent,
        ) -> None
    ```   
    The Add method is responsible of associating the given component to the group.  
    It adds the component to Group._components using the *component*'s *identifier* as a key   
    A Group can also contain other groups as components 
<br/>
<a id="Group-Update"></a>
- **Update**    
    ```python
    def Update( self,
            componentIdentifier: str,
            component: pyMDComponent,  
        ) -> None
    ```        
    The Update method is responsible of modifying the group's *_components* dict by replacing the component associated to *componentIdentifier* with the given *component*
<br/>
<a id="Group-Get"></a>
- **Get**    
    ```python
    def Get( self, identifier: str | list[str] ) -> pyMDComponent
    ```        
    The **Get** method is responsible of returning the component associated to the given identifier.    
    To get a component that is part of a child Group from the parent Group, use a list of identifiers

### Text
```python
class Text (pyMDComponent)
    _text : str
    _outText : str
    def __init__( self,
            parent : Group | None = None, 
            identifier : str | None = None,
            text: str | None = None,
            bold : bool = False,
            italic: bool = False,
            strike: bool = False,
            sub: bool = False,
            sup: bool = False,
            underlined : bool = False,
        )
    def Format( self, *args, **kwargs ) -> None
```
Child class of [pyMDComponent](#pymdcomponent).     
A **Text** is a basic component that represents text.            
It includes various styling options:
- **bold**
- _italic_
- ~~strike~~ 
- <sup>sup</sup>
- <sub>sub</sub>
- <ins>underlined</ins>

Every Text has this method:
```python
class Text (pyMDComponent):
    def Format( self, *args, **kwargs ) -> None
```
<a id="Text-Format"></a>
- **Format**   
    ```python
    def Format( self, *args, **kwargs ) -> None
    ```   
    The Format method is responsible of calling str.format() on the component's *_text* string.   
    This can be used to create a Text variable with formattable text (like `"Today is {}"`) and format it with proper data later in the script.  
    When a Text component is formatted, the component's *_outText* is updated with the formatted string

When adding a Text component to another Text component, the result is a Text component that has:
- As *_text* the sum of *self._text* and *other._text*
- As *_outText* the sum of *self._text* and *other._text*
- The same type of *self* (for example, when adding a text to a [Heading](#heading), the result is a Heading)

### Heading
```python
class Heading ( Text ):
    MAX_HEADING_LEVEL = 3
    _headingLevel: int
    def __init__( self, 
            parent : Group | None = None, 
            identifier : str | None = None,
            headingLevel : int = 1,
            text: str | None = None,
            bold : bool = False,
            italic: bool = False,
            strike: bool = False,
            sub: bool = False,
            sup: bool = False,
            underlined : bool = False,
        ): pass
```
Child class of [Text](#text).     
A **Heading** is a heading text. 
*headingLevel* could be from 1 (highest) to 3 (lowest)  
A Heading of level 1 could be created using **H1**
```python
heading = Heading( text = "Heading here", headingLevel = 1 )
# equals
heading = H1( text = "Heading here" )
```
The same thing can be done with **H2** and **H3**  

### Quote
```python
class Quote(Text):
    def __init__( self, 
        parent : Group | None = None, 
        identifier : str | None = None,
        text: str | None = None,
        bold : bool = False,
        italic: bool = False,
        strike: bool = False,
        sub: bool = False,
        sup: bool = False,
        underlined : bool = False,
    )
```
Child class of [Text](#text).     
A **Quote** is a quoted text. 

### Link
```python
class Link(Text):
    def __init__( self, 
            target : str | list[str],
            parent : Group | None = None, 
            identifier : str | None = None, 
            text : str | None = None, 
            bold : bool = False, 
            italic : bool = False, 
            strike : bool = False, 
            sub : bool = False, 
            sup : bool = False, 
            underlined : bool = False,
        ): pass
```
Child class of [Text](#text).     
A **Link** can be either external or internal.  
If *target* is a string, the link points directly to the given *target*.  
If *target* is a [**pyMDComponent**](#pymdcomponent) or any **child class**, the link points to the *target*'s anchor.

### Image
```python
class Image(Link):
    def __init__( self,
            src : str,
            alt : str = "",
            parent : Group | None = None, 
            identifier : str | None = None,
        ): pass
```
Child class of [Link](#link).     
An **Image** is... an image.  
Check GitHub's guide on [md images](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images) for a better understanding of what *src* can be