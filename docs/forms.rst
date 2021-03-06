Form Handling
=============

WebRacer recognizes the following form elements:

- input type=text
- input type=radio
- input type=checkbox
- input type=submit
- input type=reset
- input type=image
- button
- textarea
- select

Form element handling is independent from form attributes and forms themselves.

Buttons/submit fields per http://symfony.com/doc/2.0/components/dom_crawler.html:

- input[type=submit]
- input[type=image]
- button

Which submit button is chosen by default:

http://stackoverflow.com/questions/925334/how-is-the-default-submit-button-on-an-html-form-determined

I believe that Internet Explorer chooses the submit button that appears first in the source; I have a feeling that Firefox and Opera choose the button with the lowest tabindex, falling back to the first defined if nothing else is defined.

The current HTML5 working draft specifies that the first submit button must be the default:
