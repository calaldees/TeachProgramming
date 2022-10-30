Login Transition
================


Task:
Modify CSS in `start.html` so that - when the screen is clicked
* the `#background img` blurs (0.5em)
* the `#login` layer (profile circle and text box's) fades in and moves upwards and un-blurs

## Approach
1. Get the state's of the items changing on click first
    * e.g. make the login appear onclick
    * then. make the background blur onclick
2. Add the `transition: PROPERTY TIME EASE`
    * https://www.w3schools.com/css/css3_transitions.asp


## Hints
There are hints in the `start.html` file.
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