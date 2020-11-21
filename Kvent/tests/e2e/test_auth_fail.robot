*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    chrome
${URL}    https://kventeventapplication.herokuapp.com/

*** Test Cases ***
Test user sign up fail via Django auth.

Test user login fail via Django auth.

*** Keywords ***