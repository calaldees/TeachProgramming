Login Transition
================

Task:
Modify CSS in `start.html` so that - when the screen is clicked
* the `#background img` blurs (0.5em)
* the `#login` layer (profile circle and text box's) fades in and moves upwards and un-blurs

## Approach
1. Bring up devtools/inspector - see what class is added when the screen is clicked
2. Make the login appear when the class is applied to the body
3. Make the background blur when the class is applied to the body
4. Add the `transition: PROPERTY TIME EASE`
    * https://www.w3schools.com/css/css3_transitions.asp


## Hints
There are hints/stubs in the `start.html` file.
Additional hits are below.
### Required properties
```css
    /* values to change */
    opacity: 1;
    top: 0;
    filter: blur(0.0em);
```
### Active class in parent element
```css
.login_active THING THING2 {
    /* new values */
}
```
### A transition example
```css
THING {
    transition: background-color 1000ms linear;
    background-color: white;
}
THING:hover {
    background-color: red;
}
```