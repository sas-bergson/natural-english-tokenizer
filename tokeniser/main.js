text = "The quick brown fox jumped over the lazy dog. The Main miners of the world. An anthilled"
//divide into sentences
var check_sentence = (text)=>{
    split_sentence = text.split('.')
    console.log(`sentences(${split_sentence.length}):`);
    for(i = 0; i < split_sentence.length; i++){
        console.log('  -> '+split_sentence[i]);
    }
return split_sentence
}

//split into words 
var check_word = (text)=>{
    split_word = text.split(" ");
    genre = [split_word.length]
    for(n=0; n<split_word.length; n++){
        if(split_word[n].toLowerCase()=="the" || split_word[n].toLowerCase()=="an" || split_word[n].toLowerCase()=="a"){
            genre[n] = 'article'
        }
        else{
            genre[n] = 'not defined'
        }
    } 
    console.log(text)
    for(i = 0; i<split_word.length; i++ ){
        console.log(split_word[i]+`(${split_word[i].length})`+' -> '+genre[i]+'\n');
    }
    
}
test = check_sentence(text)
console.log(test.length);
for(i = 0; i<split_sentence.length; i++){
    check_word(test[i])
}
