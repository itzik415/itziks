<script>
    function clears(){    
                if(secValue > 0 && secValue < 10){ 
                        secValue--;
                        document.getElementById('timerSeconds').innerText = '0' + secValue;
                    }
                    if(secValue == 0 || (secValue <= 59 && secValue >= 10)){ 
                        document.getElementById('timerSeconds').innerText = z;
                        z--;
                    }
            }
            
            
            function ff(){
                if(document.getElementById('resetButton').onclick){
                    document.getElementById('timerMinutes').innerHTML = "00";
                    document.getElementById('timerSeconds').innerHTML = "00";
                    document.getElementById('timeChoseMinutes').value = 0;
                    document.getElementById('timeChoseSeconds').value = 0;
                    clearInterval(clears);
                }
            } 
            
            
            
            document.getElementById('submitButton').onclick = function(){
                var minValue = document.getElementById('timeChoseMinutes').value;
                var secValue = document.getElementById('timeChoseSeconds').value;
                var z = 59;
                
                if(secValue >= 0 && secValue <= 60 && minValue >= 0 && minValue <= 60){
                    if(minValue < 10 && minValue >= 0 && secValue < 10 && secValue > 0){
                        document.getElementById('timerMinutes').innerText = '0' + minValue;
                        document.getElementById('timerSeconds').innerText = '0' + secValue;   
                        function clears(){    
                            if(secValue > 0 && secValue < 10){ 
                                    secValue--;
                                    document.getElementById('timerSeconds').innerText = '0' + secValue;
                                }
                                if(secValue == 0 || (secValue <= 59 && secValue >= 10)){ 
                                    document.getElementById('timerSeconds').innerText = z;
                                    z--;
                                }
                        }
                        setInterval(clears,1000);
                        

                        
//                        if(document.getElementById('timerSeconds').innerHTML == "00"){
//                            clearInterval(sec);
//                        }
                        
                    }
                    else if(minValue > 9 && (secValue < 10 && secValue >= 0)){
                        document.getElementById('timerMinutes').innerHTML = minValue;
                        document.getElementById('timerSeconds').innerHTML = '0' + secValue;
                    }
                    
                    else if((minValue < 10 && minValue >= 0) && secValue > 9){
                        document.getElementById('timerMinutes').innerHTML = '0' + minValue;
                        document.getElementById('timerSeconds').innerHTML = secValue;
                    }
                    
                    else if(minValue > 9 && secValue > 9){
                        document.getElementById('timerMinutes').innerHTML = minValue;
                        document.getElementById('timerSeconds').innerHTML = secValue;
                    }
                    
                    else if(secValue < 0 || secValue > 60 || minValue < 0 || minValue > 60){
                        alert("You enter ther wrong numbers. You are only allowed to enter numbers between 0 - 60");
                        document.getElementById('timerMinutes').innerHTML = "00";
                        document.getElementById('timerSeconds').innerHTML = "00";
                        document.getElementById('timeChoseMinutes').value = 0;
                        document.getElementById('timeChoseSeconds').value = 0;
                    }
            
                }
            }
            
            

            
    
</script>