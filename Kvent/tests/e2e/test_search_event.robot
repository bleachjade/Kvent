*** Settings ***
Library    SeleniumLibrary
Test Teardown    Close Browser
Suite Teardown    Close Browser

*** Variables ***
${BROWSER}    chrome
${URL}    https://kventeventapplication.herokuapp.com/
${text}    Suki Suki!
# ${USERNAME}    testRobot
# ${PASSWORD}    KventTestPass12345
# ${EMAIL}    admin@gmail.com
# ${FIRSTNAME}    MR. Robert
# ${LASTNAME}    FERGUSON
# ${TEL}    0991234567
# ${ADDRESS}    99/10 A Street California USA

*** Test Cases ***
Test search keyword and verify search result on Google
    Display Kvent index page
    Input Text To serch
    Check That Is Correct Event That Has Been Searched
Teat search event that does not exist
    Display index page
    Input Text To serch Event
    Check That Event Is Not Be Found
*** Keywords ***
# test case 1
Display Kvent index page
    Open Browser    ${URL}    ${BROWSER}

Input Text To serch
    Input Text    name:query    ${text}    
    Click Button    class:submit

Check That Is Correct Event That Has Been Searched
    Page Should Contain    ${text}
#test case 2
Display index page
    Open Browser    ${URL}    ${BROWSER}

Input Text To serch Event
    Input Text    name:query    Run together    
    Click Button    class:submit
Check That Event Is Not Be Found
    Page Should Contain    No Events
