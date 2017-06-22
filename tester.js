// Write a function that will  make an array print like:
//
// 0 -> James
// 1 -> Jill
// 2 -> Jane
// 3 -> Jack

function fancyArray(test){

   for(var i = 0; i <= test.length-1; i++){

     console.log((i) + " -> " + test[i])
  }
}

var names_arr = [ "James", "Jill", "Jane", "Jack" ];

fancyArray(names_arr);
