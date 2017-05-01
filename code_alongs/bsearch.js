// arr[Math.floor(arr.length/2)-1]
count = 0;
function bSearch(arr,num){
	var itemIndex = null;
  var previousIndex = Math.floor(arr.length/2);
  var insersionIndex = Math.floor(arr.length/2);
  var insersionPoint = arr[insersionIndex];

  while(true){
    console.log(insersionPoint, insersionIndex)
    if(insersionPoint < num){
      previousIndex = insersionIndex;
      insersionIndex = Math.floor((insersionIndex + previousIndex) / 2);
      insersionPoint = arr[insersionIndex];
    } else if(insersionPoint > num){
      arr = arr.slice(0,insersionIndex);
      previousIndex = insersionIndex;
      insersionIndex = Math.floor(insersionIndex - (previousIndex / 2)) ;
      insersionPoint = arr[insersionIndex];
    } else if(insersionPoint == num){
      itemIndex = insersionIndex;
      break;
    }

    if(count > 100) break
    else count++;
  }

	return itemIndex;
}

console.log(bSearch([1,2,3,4,5,6,7,8,9],4))
