#################################
# Speech Script by Dan Fountain #
#      TalkToDanF@gmail.com     #
#################################

#can be found here:
# https://web.archive.org/web/20151016182428/http://danfountain.com/2013/03/raspberry-pi-text-to-speech/https://web.archive.org/web/20151016182428/http://danfountain.com/2013/03/raspberry-pi-text-to-speech/

INPUT=$*
STRINGNUM=0
 
ary=($INPUT)
echo "---------------------------"
echo "Speech Script by Dan Fountain"
echo "TalkToDanF@gmail.com"
echo "---------------------------"
for key in "${!ary[@]}" 
  do
    SHORTTMP[$STRINGNUM]="${SHORTTMP[$STRINGNUM]} ${ary[$key]}"
    LENGTH=$(echo ${#SHORTTMP[$STRINGNUM]})
    #echo "word:$key, ${ary[$key]}"
    #echo "adding to: $STRINGNUM"
    if [[ "$LENGTH" -lt "100" ]]; then
      #echo starting new line
      SHORT[$STRINGNUM]=${SHORTTMP[$STRINGNUM]}
    else
      STRINGNUM=$(($STRINGNUM+1))
      SHORTTMP[$STRINGNUM]="${ary[$key]}"
      SHORT[$STRINGNUM]="${ary[$key]}"
    fi
done
 
for key in "${!SHORT[@]}"
  do
    #echo "line: $key is: ${SHORT[$key]}"
 
    echo "Playing line: $(($key+1)) of $(($STRINGNUM+1))"
    NEXTURL=$(echo ${SHORT[$key]} | xxd -plain | tr -d '\n' | sed 's/\(..\)/%\1/g')
    mpg123 -q "http://translate.google.com/translate_tts?tl=en&q=$NEXTURL"
done