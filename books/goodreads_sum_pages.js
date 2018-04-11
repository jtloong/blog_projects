var sum_pages = 0, table_elements = document.getElementsByClassName('field num_pages');
for (var i = 1; i < table_elements.length; i++){
	value = table_elements[i].innerText.slice(0, -4);
	if (value !== "unkn"){
		sum_pages += Number(value);
    }
} 
console.log(sum_pages);
