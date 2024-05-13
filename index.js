const display = document.getElementById('display');

function btnDisplay(input){
      display.value = display.value + input;
}

function clearDisplay(){
    display.value = '';
}

function calculate(){
    try{
        display.value = eval(display.value);
    }
    catch(err){
        display.value = err;
    }
    
}

function deleteDisplay(){}