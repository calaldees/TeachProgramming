Login Transition

https://www.w3schools.com/css/css3_transitions.asp

Task:
Modify `start.html` so that
* the background blurs (0.5em)
* the profile circle fades, moves upwards and sharpens in

### Hints
#### Required properties
```css
    /* values to change */
    opacity: 1;
    top: 0;
    filter: blur(0.0em);
```
#### Active class in parent element
```css
.login_active THING THING2 {
    /* new values */
}
```
#### A transition example
```css
THING {
    transition: background-color 1000ms linear;
    background-color: white;
}
THING:hover {
    background-color: red;
}
```