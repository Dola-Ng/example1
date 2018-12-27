//isEven

function isEven(num){

	if(num % 2 === 0) {
		return true;
	}

	else {
		return false;
	}
}

function factiorial(num){

	var result = 1;

	for (var i=1,i<=num, i++){
		result *= i;
	}

	return result;
}

function kebabToSnake(str) {
	 var newStr = str.replce(/-/g,"_");
	 return newStr;
}