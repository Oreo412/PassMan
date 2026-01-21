const fileInput = document.getElementById('fileInput');
const fileContent = document.getElementById('fileContent');
const password = document.getElementById('passwordIn');
const decryptButton = document.getElementById('decryptButton');
let passwordsJson;


var reader = new FileReader();
    


reader.onloadend = function() {
    getJson(reader.result);
};

async function readEncryptedFile(){
    console.log("running...")


    reader.readAsArrayBuffer(fileInput.files[0])
    
}

async function getJson(content)
{
    const decoderguy = new TextDecoder()
    console.log(decoderguy.decode(content))
    const salt = content.slice(0, 16)
    const nonce = content.slice(16, 32)
    const cipherText = content.slice(32)
    

    const key = await getHash(password.value, new Uint8Array(salt)).then((hash) => createKey(hash))

    
    
    passwordsJson = await decryptData(key, cipherText, nonce)
    for(site in passwordsJson){
        const createElementTest = document.createElement("p")
        createElementTest.id = site
        createElementTest.innerText = site
        document.body.appendChild(createElementTest)
        console.log(`Site: ${site} \n Username: ${passwordsJson[site].username} \n Password: ${passwordsJson[site].password}`)
    }

    
    
    
}

async function createKey(key){
    let outputKey;
    try{
        outputKey = await window.crypto.subtle.importKey("raw", key, "AES-GCM", true, ["decrypt"])
        console.log("Key Created Successfully: ")
    } catch(err)
    {
        console.log("Error creating key: " + err)
    }

    return outputKey

}


async function getHash(password, salt){
    return argon2.hash({
        pass: password,
        salt: salt,
        time: 3, // the number of iterations
        mem: 65536, // used memory, in KiB
        hashLen: 32, // desired hash length
        parallelism: 4, // desired parallelism (it won't be computed in parallel, however)
        type: argon2.ArgonType.Argon2id, // Argon2d, Argon2i, Argon2id
    })
    // result
    .then(res => {
        console.log(res.hashHex)
        return res.hash
    })
    // or error
    .catch(err => {
        console.log("Error handling password: ", err.message)
        return null
    })
}


async function decryptData(key, cipherText, nonce){

    
    try{
        const plainText = await window.crypto.subtle.decrypt({ name: "AES-GCM", iv: nonce, tagLength: 128}, key, cipherText)
        console.log(new TextDecoder().decode(plainText))
        fileContent.innerText = new TextDecoder().decode(plainText)
        return JSON.parse(new TextDecoder().decode(plainText))
    }catch(err){
        console.log("test");

        if (err instanceof DOMException) {
            console.log("testw");

            console.error(`Error Name: ${err.name}, Code: ${err.code} Message: ${err.message}`);
        } else {
            console.error("Unexpected error:", err)
        }
    }

}



function buf2hex(buffer) { // buffer is an ArrayBuffer
    return [...new Uint8Array(buffer)]
        .map(x => x.toString(16).padStart(2, '0'))
        .join('');
  }