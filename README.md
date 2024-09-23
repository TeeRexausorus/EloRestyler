Franchement, flemme de faire un readme, alors :
`mkdir output`

`docker build --build-arg GEMINI_API="<api_key>" -t elorestyler . && docker run -v $PWD/output:/output elorestyler`
