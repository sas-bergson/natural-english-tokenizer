word = "The quick brown fox jumps over the lazy dog";
var check_word = (text)=>{
    split_word = text.split(" ");
    genre = [split_word.length]
    for(n=0; n<split_word.length; n++){
        if(split_word[n].toLowerCase()=="the" || split_word[n].toLowerCase()=="an" || split_word[n].toLowerCase()=="a"){
            genre[n] = 'article'
        }
        else{
            genre[n] = 'noun'
        }
    } 
    console.log(text)
    for(i = 0; i<splitword.length; i++ ){
        console.log(splitword[i]+' -> '+genre[i]);
    }
    console.log(genre)
    
}
check_word(word)