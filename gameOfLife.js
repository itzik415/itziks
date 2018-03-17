
var list = [['.','.','.','.'],
            ['.','L','L','L'],
            ['L','L','L','.'],
            ['.','.','.','.']]

var countNeighbors = function(i,j){
    var count = 0;
    for(var k = i-1; k < i+2; k++){
        for(var l = j-1; l < j+2; l++){
            if(k >= 0 && l >= 0 && k < list.length && l < list.length){
                if(list[k][l] === 'L'){
                    if(k !== i || l !== j){
                        count++;
                    }
                }
            }
        }
    }
    return count;
}

function isAlive(i,j){
    if(list[i][j] === 'L'){
        return true;
    } else{
        return false;
    }
}


var applyRules = function(count,isAlive){
    if(isAlive){
        if(count < 2){
            return ".";
        }
        else if(count >= 2 && count <= 3){
            return "L";
        }else{
            return '.';
        }
    } else{
        if(count === 3){
            return "L"; 
        }else{
            return ".";
        }
    }
}




function gameOfLife(list){
    var list2 = [['.','.','.','.'],
                 ['.','.','.','.'],
                 ['.','.','.','.'],
                 ['.','.','.','.']]             
    for(var i = 0; i < list2.length; i++){
        for(var j = 0; j < list2.length; j++){
            var count2 = countNeighbors(i,j);
            var alive = isAlive(i,j);
            list2[i][j] = applyRules(count2,alive);
        }
    }
    return list2
}

var newList = function(){
    list = gameOfLife(list)
    console.log(list);
}

setInterval(newList,1000);