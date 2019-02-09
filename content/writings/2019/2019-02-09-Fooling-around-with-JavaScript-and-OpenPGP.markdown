---
title: Fooling around with JavaScript and OpenPGP
author: Oz Nahum Tiram
published: 2019-02-09
tags: JavaScript,cryptography
public: yes
chronological: yes
kind: writing
summary: >
    Fooling around with JavaScript and OpenPGP, as the title says. I needed to
		create a page in which I can encrypt files with OpenPGP. Doing this with JavaScript
		turned out to be possible. These are the results of my experiment.
---

Recently, I found myself using GnuPG more often. The background is that I want
to create a website which allows users to send a message with attached files
to the site owners. At first, I was looking at creating some kind of CMS with
a file storage on the server. But then I decided I don't want to have any files
on the server. E-Mail isn't a good solution if one wants also to send files with
personal data.
The solution I thought of is sending a message with attached files asymmetrically
encrypted with a public key. This turned out easy and not so easy. The website
I created is using Python for the back-end. There are few Python libraries to
interact with GnuPG. However, encrypting files on the server means that the file
is uploaded to the server and is only then encrypted. Not a big issue with HTTPS
connection, but it is nicer if one could encrypt the file already in the Browser.
This is where OpenPGP enters the picture.  

[rant] This library was not easy to understand for me, because I am a
spoiled Pythonista. Meaning: usually there is a much better documentation for
the libraries I am using.[/rant]  

I found a few online examples but not a fully usable working example except
for one example using OpenPGP in version 2.3. This looked dangerous, especially
in the light of known CVEs in earlier versions of this library.
So, I decided to try and mess around with JavaScript and port the little project
to a newer version of the Library. You can find the [the result][1].

The code for encrypting the file is simply straight forward:

```javascript

function getKeyList() {
	var keysList = []
	var pubKeyData = queryAll('.public-key textarea').map(el => getKey(el, 'public'))
	pubKeyData.forEach(async function(key){
		var l = (await openpgp.key.readArmored(key)).keys[0]
		keysList.push(l)
	})

	return keysList;
}

query("#uploader").addEventListener('change', function() {

	var reader = new FileReader();
	reader.onload = async function() {

		var arrayBuffer = this.result;
		var fileData = new Uint8Array(arrayBuffer);
		var keys = getKeyList();
		const options = {
			message: openpgp.message.fromBinary(fileData),
			publicKeys: keys,
			privateKey: "",
			armor: true,
		};

		return openpgp.encrypt(options).then(results => {
			link = document.createElement('a');
			link.setAttribute('href', window.URL.createObjectURL(
			new Blob([results.data]), {type: "application/pgp-encrypted"})
			);
			link.setAttribute('download', "encrypted.file.gpg");
			link.innerHTML="encrypted.png"
			query('#output').appendChild(link);
		});


	}
	reader.readAsArrayBuffer(this.files[0]);

}, false);
```

But what's not so straight forward is working with Promises in JavaScript.
I spent quite some time trying to grok this, I still lack some aspects of working
with `async`, `await` map function with JavaScript. The code could be written
in a much nicer way I guess. Suggestions are welcomed.

[1]: https://github.com/oz123/gpg-online
