// Tuesday Warmup
// Bubble Sort

'use strict'

function bubbleSort(arrayToSort){
  let sortIterator = 0;

  const sorted = (arr) => {
    let sorted = true;
    for(let i=0;i < arr.length-1; i++){
      if( arr[i+1] < arr[i]){
        sorted = false;
      }
    }
    return sorted;
  }

  while( !sorted(arrayToSort) ){
    let poppedItem;

    if(arrayToSort[sortIterator] > arrayToSort[sortIterator+1]){
      poppedItem = arrayToSort[sortIterator+1];

      arrayToSort[sortIterator+1] = arrayToSort[sortIterator];
      arrayToSort[sortIterator] = poppedItem;

    }

    if(sortIterator <= arrayToSort.length){
      sortIterator++;
    } else {
      sortIterator = 0;
    }

  }

  return arrayToSort;

}

// console.log(process.argv[2])
console.log( bubbleSort([65,32,87,54,100,5,4,9,8,7,6,5,34,87,3,4,4,3,2,1]) )
