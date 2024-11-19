*** Settings ***
Resource  resource.robot
Test Setup  Input New Command and Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  uus  salasana123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  vanha  salasana123
    Output Should Contain  User with username vanha already exists

Register With Too Short Username And Valid Password
    Input Credentials  u  salasana123
    Output Should Contain  Username may consist only of letters a-z and be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  uusi1  salasana123
    Output Should Contain  Username may consist only of letters a-z and be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  uus  lyhytt7
    Output Should Contain  Password must be at least 8 characters long and must not consist only of letters.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  uus  kaheksan
    Output Should Contain  Password must be at least 8 characters long and must not consist only of letters.
  

*** Keywords ***
Input New Command And Create User
    # luo ensin joku vanha käyttäjä
    Create User  vanha  salasana123
    Input New Command