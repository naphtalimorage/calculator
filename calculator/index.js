const display = document.getElementById('display');

function appendToDisplay(char){
      display.value += char;
}

function clearDisplay(){
    display.value = '';
}

function calculate(){
    try{
        display.value = math.evaluate(display.value);
        console.log(display.value);
    }
    catch(err){
        display.value = err;
    }
    
}

function deleteDisplay(){}