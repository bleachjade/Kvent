*** Settings ***
Library    SeleniumLibrary
Test Teardown    Close Browser
Suite Teardown    Close Browser

*** Variables ***
${BROWSER}    chrome
${URL}    https://kventeventapplication.herokuapp.com/