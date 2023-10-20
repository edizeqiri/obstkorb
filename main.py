# Import the libraries
import string
from Levenshtein import *

# Define two long strings without spaces
string1 = "3db8a17a1a02300e3db8a17a1a02300ef0906d688e1c837052225e823db8a17a1a02300ee6c09da25f34423a214c6c3486a42f42e878d0ab57af23dec61b6f181bddbcaac7593c3db8a17aeb8b2e4b1a02300e3db8a17a2cb52f085fbe7ff41a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300ec19ce261a02300e8112ce49535a96ef93f9bc6e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300eccab38bb3db8a17aeb8b2e4b636088ceab698f6ae641ab5e3db8a17a1a02300e1a02300ea0f570c03db8a17accab38bb1a02300e3c9c6a09455a4e33db8a17aeb8b2e4b82419fc9c21014d51a02300eaad1cca1a02300ee1c291e3aac7593c1a02300e7343ae4263676001fcfbe38f1a02300e37b74b86149c2da441053dc81a02300e437ecbc2a1ca43a81a02300e4b2caf4167fe5c84d87a675b4c59cb5ad4833a2baac7593ced16effd97c7a9401a02300e73352ff1f2da6692fcfbe38fd9cb86c41a02300e8bb81004e9afe0883db8a17a1a02300e3db8a17a836a726bf1c6c8ea4a8743f620155312aac7593c455a4e33db8a17a3db8a17a1a02300e77c3980b643a5b1b7c91cb3a6703a593cdbeb8aece3b9113449b7f8dd7b70765149c2da4f67edfe64dba4218ccab38bb1a02300ede6c37d57c91cb3a3db8a17ae8484ae53e988c081a02300efb3c5a313db8a17a1a02300ec1937ef13db8a17a97c7a9409fce187d97a0c600214c6c3ccab38bb1a02300eccab38bb1a02300ec19ce261a02300e2a411bd13db8a17a8874393b1a02300e149c2da4cdbeb8ae4b61e891a02300e1a02300e1703253d1a02300ebe6cb40e1a02300e90f667c78d04657984e57ff0d9cb86c46ad9b0f167fe5c84d3a88209455a4e3b06554481a02300e67fe5c84dad0ef0363afd50a1a02300e29e580511a02300e30685a1c3db8a17accab38bb3db8a17a1a02300e4345b1ef87bb176b3db8a17a41053dc8a00999771a224934ccab38bb1a02300e1a02300e3b2fc8983dccc183db8a17a149c2da4bdfa08a7fcfbe38f263dee8c1fd083a7f57321a3e453265332f789dc1a02300e1a02300e1a02300e1a02300e78958d0b3e19bffce46ca9642afcccd67fe5c84f175015881b6851d7627382f61af203d1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e65d3c2284dba4218814087e3535a96efdcdcd29c27f7976b149c2da4ccab38bbb619b771a02300e27f8ab2a1a02300e3db8a17a1a02300e91f1e2dc1a02300e1a02300eaac7593ce6a82ee411fde3f1a02300e3db8a17a5f34423a3bca60e1a02300e1a02300edfa1a8711a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e653e3deac19ce26c4d3411e1a02300e1a02300e1a02300e3d5f6c413db8a17a1a02300e83d1b65344c2d4b838417b991a02300eaac7593c93298eff3db8a17acbd7c3c767fe5c84181bddbc1a02300e3db8a17a3db8a17ae75426013db8a17a349bd05d7d4e2019a255bece91f1e2dce136fb7391f1e2dc91f1e2dc5b3d5bda7d4e20197d4e2019ccab38bb1a02300e67fe5c84da4499587631ae9c3db8a17a512fbc2444c2d4b81f4037de11a0e9371a02300e3e988c083db8a17a4fa9b5a035db3be31a02300e1a02300e1393cf893db8a17a1a02300eb930c803381f185c418f07e43e988c0849e8c20528683ea83db8a17ae23f299c1a02300ecb64b5f11fde3f3db8a17a149c2da4c5b9d5347d4e20191a02300e69ed2ac9b5db0a3a0cc5aaeb2f8d1c65c763af01a02300ee949b7531a02300e3db8a17a149c2da41a02300e1a02300e27a77001cdbeb8ae2ece737deb8b2e4b655c92571a02300e700a6cabab698f6a3db8a17a3db8a17a3db8a17a3db8a17a3db8a17a5b40bf3f1a02300ed796a62a37dcdc481a02300e7d4e2019"

string2 = "5c381fe4c7f48c3a1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1b522b3c1a02300e3db8a17a57fc18bbbb78c80f117fdefe63afd50a1270a4991a02300e7c91cb3a1a02300e1f6496933db8a17a4ac25a95bdc23df6d6294105aac7593cccab38bb825ce0fbe5bd86d71a02300eccab38bb3db8a17a7c91cb3a6249a7c11a02300e1a02300e1a02300ec137aa513db8a17a10624ac4ccab38bb439ac39cccab38bb240d963eccab38bbab698f6a1a02300e1a02300e1e537f40eee9d866eee9d866eee9d866eee9d866eee9d866eee9d866eee9d866eee9d8661a02300e1a02300e6ec2dea61a02300e1a02300e1a02300e3db8a17a1a02300e1a02300e1a02300ece1da44e1a02300ed6fb251d1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300eba6f1e708f3c41563db8a17a6cebaf3b32f789dc66977a5c1a02300e1a02300eaac7593c1a02300e1a02300e4e72536076114bab1a02300e1a02300e3db8a17a5122d931a02300e1a02300eb6271271b6271271b6271271d99e1ecd99e1ecd99e1ecd99e1ecd99e1ec2723a789fcf1c1882cba82f2a77972707c8635706bf35dfb12a198211a02300e1a02300eaac7593c9a97c6a71a02300e1efc5d10aac7593c1a02300e1a02300ed4a3d22daac7593c1a02300e1a02300e26310c661a02300e29e580513db8a17a683c13cc1a02300e3db8a17a1a02300e441fe52dd9ad801632fb44c51ab51a11a02300e51ab51a18d124d17235134331a02300e7d4e2019cf82aa415983d7f41a02300e1a02300e7c91cb3af08d35011a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300ed6d8c26e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e51ab51a195275ed351ab51a195275ed3bd13615edadcca578f5e68f2a58bd0c768adc671a02300e6f5fb5168773834555684611a814dbf735b4c19ee2da2fc76c6e4752fcff9ded98b68787d60fd371db95a0ef7dac469842608bbe5f934d5dfd26898e5f934d54f28d1051a02300e1a02300e295621bbd2606e4ccc0ac9409618789ed3fa94a1a02300e1a02300ea4e857311a02300e3b839a9a1a02300e1a02300eca44a9201a02300e7c0fa97695275ed395275ed351ab51a1dadaee8a4f28d1054f28d10595275ed31a02300e27d0c6df27d0c6dfc19ce26c19ce26c19ce261a02300e1a02300e1a02300e1a02300eea47a5b01d119022ea47a5b051ab51a1b94f872ed97da8274a48f792ea47a5b036e391e227d0c6df9a97c6a7ab698f6ae35a3d4f1bfd93544f38df963db8a17a1a02300e6249a7c11a02300e1a02300e3db8a17a3db8a17a9618789e1a02300e3db8a17a1a02300e1a02300e1a02300e1a02300e3db8a17a1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e45cf2fbaaac7593cab698f6a1a02300ebdd20f9d1a02300ebdd20f9d1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300eaac7593c1a02300e11fde3f7eabe427ccab38bb3db8a17aa57b86678efe597d9132314d1a02300e1a02300eb23f4443cac70f8cea47a5b06efb40a93adfbf768d937c2d1724f8b21a02300e1a02300e3da1db67ccab38bb5692ce0123a9ceeb1724f8b26e41a808aac7593c84c339313db8a17a1a02300e69f01dedc3e665f33adfbf761a02300e76d2438755a248711a02300e3db8a17a68d15d47a9ffcecb573d419bd62215258ab42dbd1a02300e1a02300e1a02300e3db8a17a3db8a17a1a02300eea47a5b03fc28c181a02300e1a02300e8a08ff2c3db8a17a7b7485b1408ac0b830fd34891e5193a63db8a17a1c315cb995275ed31a02300e95275ed3ab698f6a1f26b076bdd7b1202dfb455b1a02300e2adbeb3b13e9e668481a57a21a02300e4bc1be0baac7593ca5c3e07f3db8a17a73d1688687ea59703bea77838eb92c32f136a39ccab38bb7c91cb3accab38bbb3fb02511a02300eccab38bb404e5fe5666588281a02300e3db8a17a6249a7c157c44fabab7e41173db8a17a7c91cb3a50498fce1a02300e1a02300e1a02300e28d5496818152c81a02300e3db8a17a48a855d56cd1e0ea3db8a17a8292745a1a02300ec3e665f3c19ce2651ab51a11a02300e1a02300e3adfbf766dc312f38616072a65f3ba144e079e6c80a35f27b515c60485e90a211a02300e77ea4e33105710d23db8a17ad9c9a0ff8bedcafb1a02300e1a02300eccab38bb1a02300e3b628f321a02300e1a02300e1a02300eea47a5b04c72766b1a02300e36beb7a83db8a17a7c91cb3a1a02300e1a02300ee6daa6831a02300e1a02300e57c44fab1a02300e1a02300e1a02300e1a02300e814643d89765b67e1a02300e1a02300e457220821a02300e74be6da91a02300ed2a4ff70b23f44431a02300e1a02300e72ceb6634aa8245e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e11db71851a02300e1a02300e8111a7181a02300e7c91cb3a1a02300e1a02300e1a02300e1a02300e1a02300e5cb33e8fe2c1a43db8a17a1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300ecf2349581a02300e7c91cb3a1a02300e1a02300e1a02300e4d38cc461a02300e1a02300e6f752152413f94861a02300e1a02300e1a02300e1a02300ec776fc4d1a02300ef43c02ca63a110b81a02300e1a02300e1a02300e1a02300e152514d711fde3f1a02300e1a02300efa77b2bd1a02300ef3077402ab698f6a7b74d5db64b54679cd994ad41a02300e1a02300e1a02300ec6e33a9c1a02300e4a99e0891a02300e4e261d4d1a02300e1a02300e1a02300e1a02300e7c91cb3adcd04e23db8a17a3db8a17a1a02300e1a02300e1a02300ea510d82c3db8a17a220208801a02300e1a02300e8c22784429e580511a02300e1a02300e1a02300e6149a9feb569b83a1a02300e1a02300e1a02300e3db8a17a8640949d782cdddeab698f6abf05592f6d49141917786ae38640949dd0cd6f861a02300e1a02300e8ca9c18b2b36c4c02612133eb23ab5c1a02300e1a02300e1a02300e1a02300e1a02300e3245345d1a02300e1a02300e1a02300e1a02300e1a02300e356abc771a02300e4ac25a9543cf3ab43a2b1be81a02300e260927ddb95395cd2cc07bca1a02300e1a02300ed6f334a0cb7aeae9d328616877d1871f085eafe98e0a1ee567a07c0b28a135c8b793cb63adfbf761a02300ec19ce261a02300e1a02300e1a02300e1a02300e1a02300eaaaf827311fde3f11fde3f1cb3aacfe1c02d0a1a02300e6eff34543bca60e18aa8b41525783769e7839112bd900d647e462d1a02300e1a02300e1a02300ef251ba31672c790042f938cbb03fc163573c5e0fccab38bbccab38bbb657fb40d6ad8fcb352b9e41ba4fc83f6249a7c15713ec0255fe73f7c91cb3a1a02300e1a02300e1a02300e399b75941a02300e1a02300e1a02300ed132281e7c91cb3ace1af4081375132e3db8a17a7b44704eccab38bb1a02300eaf691dc01a02300e7c91cb3a3d8f1ad7288018d5961e05bcfcd9021fc26490a21a02300e1a02300e1a02300e1a02300e871b26bf3db8a17accab38bbdf88673c489b66211a02300efbce515e1a02300e5b17ccf11a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300ef57321a31a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e3db8a17a1a02300e1a02300e1a02300ef3077402ea47a5b03db8a17a47e5d6fd1a02300e42e23e53db8a17aba2309ae11d9efc4848d9bc1a02300e6249a7c1f5c92f2aea47a5b051ab51a1a2b826c91a02300e1a02300e37434424b6fccbb93db8a17a3db8a17a5f50a143e8d4712e9c74837c0fa97648a855d51a02300e127f5c3d1a02300e5f6f17ef27d0c6df1a02300ec3e665f3dadaee8ac19ce26c8f26fd01a02300e7c91cb3a1a02300e1a02300e1a02300e64deb879a166dbad3a37ad39c8f26fd0127f5c3df3db1fc5dadaee8a3a37ad39578105861a02300e1a02300e3a37ad3925adb6063db8a17a1a02300e3db8a17a3db8a17a1346e5ab127f5c3d1a02300eab8f71dd1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300eab698f6a4e33e4f6154ee7aeab698f6a27d0c6df1a02300e1a02300efb6e2188cd914bd5bf4e8b60c8a3533adadaee8a3a37ad39a749d9ed1a02300e1a02300e1101e9c7c8ae61c63db8a17accab38bb1a02300e34b01bc01a02300e832cc7083db8a17a3ec98ebacca95adf4cdfa9a496b78bcdf780cdd7a0d8f605b976bc45fe8bfeec7e8215e4abb67652da2eed8890067f12b5668a8a70daafb8c279bd4331d15c0a3c561750c8f26fd0ad3fe7401a02300e1a02300e1a02300e2ca25123dfc9686f1a02300e1a02300e1a02300e1a02300e1a02300e1a02300eaac7593c1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300eb3a4683fbe5f00761a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e3db8a17a1a02300e1a02300e3db8a17af52584881a02300e1a02300e1a02300ef5ff25c91fa3596dd63f775c1a02300ed51349b21a02300e1a02300e1a02300e1a02300e1a02300e1a02300e542c06021a02300e88d146b41a02300e1a02300ed35f400dbed1a3551a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e52707bc11a02300e1a02300ec18bf3465cb33e8f1d2fdfc8c19ce267c91cb3a3db8a17aac1d3c91a02300e1a02300e6ef2c72795afb8fd6e30e94dfd3578b7866947a8473eed7a1a02300ec4d3411e4260ec1dc4d3411e285167ac2f196591a02300eedacbb51a29cfefc1a02300ebb02e8861a02300e1a02300e1a02300e7c91cb3a1a02300e1a02300e1a02300e86807738114f6af73db8a17a3db8a17a3db8a17a1a02300e1c7d214a865c61dd349c2c7d57ed91d73cb25543db8a17ad1a617e710acaa21ca2c6f46fc210aee1d119022454cdf66c19ce26a284842b3db8a17a3db8a17a72dd6d7d3db8a17a3db8a17a3db8a17a1a02300ec414174e3db8a17a3db8a17a3db8a17a3db8a17a1a02300e26c6f1e27be48f1d26b46caf8957a9dd3db8a17aefe1a02755433d399dc0bf71af66fd083db8a17accab38bbccab38bbccab38bbccab38bb14f6b4d2ca2c6f46a8024fb9a90304d33d2bbb59ee75a159ccab38bb49aad59e1a02300ea5c5761c26333059326ee934e06023048fce5ebf31650a161a02300e40b590215f4d4f26c4d3411e1a02300e677dd9ea3db8a17accab38bb1a02300e5c9b65d4eeb738a4b0f787c21014d5842f894cc19ce265613897eccab38bb1a02300eecc80ae95ba5fea046fc543790ce6502933d89ccbd1dbcfae28f5e3cb3d9614ccab38bbba04ded99aa480ab8a25e6a01473c0c91a02300ef459083fb4e3491230f2f0c7c6817a731a02300e7c91cb3a6e30e94d7c91cb3a6e30e94d7c91cb3a6e30e94d6e30e94d637f10226e30e94d1a02300edb4ee77a52e9edb77f36a8523db8a17a1a02300e4ccb6fe4c6729c52f5bc38df3153fbffd3171171a02300ed6e4fe6351eabfe9b72ab2f5c4bd5d97c4bd5d97757581181a02300e1186906f1a02300ec2cd048e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300ed2640d656e30e94d1a02300e97a689801a02300ebcb5cbce1a02300e19befd7914fbca552ef13cb15b13e52d8cfa1ec2a7e678fb79af76431b9febbba23b6202673f5b7b3859823a22fa3963d993cd404360991b45056a5795562e288a78023a877c2d23e4abf01339115bf069861ee7b7218de6df3847e329f6ccc71a02300eb86f56cfe294dcad1a02300ea730a1f11a02300edaeac0a9d6520c8416e8d13b1a02300eaac7593c812703413ed90fc549700d23ab7462bff53c3426b0b05fccab698f6ae42597fdcbd7c3c776dc754f220177e2c4d3411e505327e6f2a931568d4419105f1bab656dad0627d493f7e0b816a784a3f1a47336340ccae68054c56d6100edccfa5f1eda65e91434b450cc162c96ddf365564322b2897895275ed3cd3fb63a4afd9143cb27561b22eb42f56d58eaa3ab698f6ac00e4523db8a17a6249a7c12e831ae61a02300e3db8a17aa048d5011a02300e1a02300e1a02300eb28d9e723adfbf76d5afb14d9f2e343f1a02300e1a02300e91d616bf95275ed3be2ba7ad95275ed391d9b9e5bb0be2f21a02300e27d0c6df3adfbf76127f5c3d11fde3f3db8a17a3db8a17a5d4c46c5bd4715d6cd1e0ea68188448127f5c3d1a02300e127f5c3d95275ed3ba161e2991d9b9e527d0c6df1a02300e1a02300e6d042c191a02300e34afdf5ccab38bb6cd1e0ea1cf6e1755caaa3ec1a02300ef43c02cab23f4443b23f44431a02300ec3e665f33db8a17accab38bbc3e665f3c19ce267b5fd4d41a02300e3db8a17a6cd1e0ead5afb14dac1394428c6302ede52f50211a02300e5ea9207a3db8a17a1a02300e474a6b96c19ce261a02300e3db8a17a9132314dc3d041ca1a02300e1a02300e48a855d582d6fdfeccab38bb28f90a111a02300e1a02300e1a02300e1a02300e3db8a17a9d8e95921a02300e1a02300e3db8a17ade9507401a02300e3db8a17a6cb824eb1a02300e868077381a02300e408ac0b8b23f44431a02300ec3e665f37c91cb3a1a02300e1a02300e1a02300e2af61b391a02300ea37b847c7c91cb3a1a02300e1a02300e7c91cb3a314dc8021a02300e1a02300e7c91cb3a1a02300e1a02300e1a02300e1a02300e3db8a17ae925150e1a02300e1a02300e3db8a17a6cd1e0eaa7d689493db8a17a2149b0ccf5520d361a02300e3db8a17a8a2644981a02300e1a02300e1a02300e1a02300e1a02300e4e72536020a85246ba161e29127f5c3d1153f3d6e6179c0c8bbb49891153f3d6e642c09fa54fe484b966c940b54235624c46e4329518cb9c38eaa3e3e712634e712634ccab38bb3db8a17ae642c09ff2a931561a02300e121474e3eddb0675fbaf681e1a02300e7c91cb3a1a02300ed02805cece1da44e7c91cb3a7c91cb3a401f2da2e34c2eac19fd6b77c91cb3a3c46ccef8cdcb7204ac25a951a02300e1a02300e95ff63c57c91cb3a7c91cb3a7541618bdedec9e82cbaa3c6c21014d57c91cb3a7541618b8d5a54024e079e6c8c49f5f995ff63c578f6d99d1a543ab5ab698f6aab698f6a1a02300e3c39111d1b7fc6a06aca32073db8a17a1a02300eab698f6ae2c9e8471a02300e1a02300e1a69192722e5c2407c91cb3a7c91cb3af0c7756ba0d8f6056e30e94de78c6a90a6166b84d79862a1ab698f6a50e53ece7a5dc6386cb2d0ce86bb86567f8ee42ff115d9c8c94f981528d72bb976bc45cd92dbb6d0e42d2bb93ab16070daafb8378fd32b833152e76e30e94d5452a43f30e9df1dc71dc0d17c91cb3a7ea969bc28df494d2bcbd49f372291f265d0067634b61fafe22ef2c84564c3581a02300e34bd48a51a02300e2cff7971a02300e295621bb1a02300e1a02300ed1983cb7dcf83952149c2da4c19ce265e9d2c621a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e7f24e9b1a02300e1a02300e1a02300e1a02300e1a02300e2cc07bca1a02300e1a02300e1a02300e1a02300eccab38bb1a02300e1a02300e1a02300ee724aa646405a6991a02300e1a02300e6ef2c7271a02300e803e6c9e1a02300e1a02300eab698f6a1a02300ec93fc6311a02300e65660aa21a02300e1a02300e1a02300e1a02300e5be0bf50bad21d8c1a02300ece1da44e1a02300e1a02300e1a02300e1a02300e1a02300e"

string3 = "c46b1a02300e3db8a17a887b2821dac2d1f1df85c8962b054101e1af8d651a02300eaeebf4243db8a17a1a02300e28b024b92ae501bb1a02300e3db8a17a356abc771a02300e1a02300e89fb8147ccab38bbd9feb87b1a02300e1a02300e1a02300e1a02300e3db8a17a679da27c1a02300e3db8a17ae9dc36441a02300e1a02300e3db8a17ad6423c2dcf5788211a02300e1a02300e288159bf21c5b1139dfdc46b1a02300e33af247f1a02300e1a02300e1a02300eef37deb11a02300e8f9388711a02300e3db8a17ad9d518e61a02300e1a02300ed4e23db41a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e3db8a17a887b282124aec6903db8a17a766f6fc11c3eb4e43db8a17accab38bb1a02300e1a02300e1a02300e1a02300e1a02300eaa4cc200cd30babd60a4c3872951473bcd30babd7fee17319963064b9c02c312a9ed64833876fae9752cd6c8610d7faa9be81e1a1a02300eccab38bb3db8a17abf1f12af1a02300ecd655cb1a31776451c7d214a1c7d214a1a02300e1c7d214a1a02300ed083808286855d881c7d214a1c7d214a1c7d214a487ad2db1a02300e7d43dc2b1c7d214aa3eb90b9c2c5ebb31c7d214a1c7d214a60981bf74f1d9a0b4a2c1df61c7d214a60981bf7cccf89a2a9539ddda5cc3458487ad2db2dd383fb6699d5c615101b3f7f16a251a02300e1a02300e1a02300e68d030461a02300e1a02300e1753168d1c7d214a1c7d214ab12e0d302faa3763abf1e6821cbc4c7f4cf73747548b58cec013fe1da2bae06b449d5b6e2d805395d7b94fe0c45a2a40d208d3a31ec79225b6032a0d6b2b2a0a81609fa38b08b99b29a7575e68272e9cae20c8c9787295ad77ee3d263871b1f1ec792210372b1fabf1e682d33c1eb889f4e73fb58aeeb91f2f6ac013fe1da2bae06b449d5b6eebdb59ca38b08b991fb03c68c45a2a407e4679f627f65c3b17ea4f278bc95c5ee4e0195a28c260a1a890cc61b99d2f58439128968e798b1a1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e5612f7fe888c2c241a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300eccab38bb1a02300e1a02300e1a02300e286d52cc2679af911a02300e1a02300e8280edf21a02300e4a4db7c01a02300e1a02300e1a02300e1a02300e9ae36ffd43b55b061a02300edc0fb61a1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e8e16cab2ae501bb1a02300e1c7d214a1c7d214a1a02300e1a02300ed9ca92631a02300e2144193b1a02300e2144193b1a02300e1a02300ed733ea11c7d214ad9ca92632ae501bb2ae501bb2ae501bb2ae501bb2144193b1a02300e1a02300e2144193b1a02300e1c7d214ad9ca92631cc7830c3db8a17a3db8a17ad733ea11a02300ed733ea11a02300e3db8a17ad733ea12144193bccab38bb1a02300e1a02300e1a02300e2144193b3db8a17ad2d68a191c7d214a356abc772ae501bb2ae501bbcaf771c6d733ea11a02300ed733ea11a02300e44cb22a61a02300e1cc7830c1207dbca2ae501bb694f25e61a02300e694f25e6d733ea1d733ea11a02300e1c7d214a1a02300eccab38bb1a02300e57b530842144193b888c2c241a02300e8c6609d82ae501bbd733ea144cb22a62ae501bb1a02300ed733ea1caf771c696c37c2c1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e11fde3f1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e53d8991a1a02300e1a02300e1a02300e1a02300e1a02300e3db8a17a1a02300e1a02300e4ac25a951a02300e1a02300e3db8a17a3db8a17a1a02300e3db8a17ad4e23db44ac25a951a02300e1a02300e1a02300e94d996571a02300e"

string4 = "e61a02300e84e57ff03db8a17accab38bb3db8a17a4c59cb5a1a02300e1fd083a73db8a17a1a02300e78958d0dec61b6fccab38bb1a02300e1a02300e1a02300eb57af23fb3c5a314dba42183db8a17aeb8b2e4b3db8a17adea451ce455a4e31a02300ecdbeb8ae3db8a17a4345b1ef1a02300ea0f570c0e6a82ee48112ce498bb8100437b74b86149c2da41a02300e4dba42181a02300ed9cb86c41a02300e73352ff1aac7593ced16effd97c7a9401a02300eccab38bb1a02300e3db8a17a1a02300ec19ce261a02300e636088ce1a02300eb619b771a02300e3db8a17a1a02300eab698f6ae641ab5e3db8a17a1a02300ef2da669263afd50aa0099977ce6819356ad9b0f177c3980b149c2da47627382f67fe5c843bca60e1a02300e1a02300edfa1a87190f667c7535a96ef3e988c083b2fc89d3a8820932f789dc1a02300e1a02300e1a02300e1a02300e535a96ef1a02300ece3b9113a1ca43a8b065544881b6851d1a02300e61af203d1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e3db8a17accab38bb3c9c6a09181bddbce453265367fe5c843db8a17a52225e82214c6c32a411bd18d04657942afcccdaac7593cde6c37d54b2caf41455a4e31a2249347db231791a02300eb481dc317c91cb3accab38bbaac7593c41053dc891f1e2dc1a02300e1a02300e1a02300e1a02300e3db8a17a5f34423a87bb176b3db8a17a8874393be9afe088c1937ef1dad0ef03bdfa08a7486a42f4149c2da4455a4e311fde3fd87a675b27f7976bccab38bb3db8a17a2cb52f08149c2da49fce187dbe6cb40e1a02300e263dee8c67fe5c84aac7593ca8f18f5441053dc81a02300efcfbe38f449b7f8df1c6c8eafcfbe38f1a02300efcfbe38f5f34423adcdcd29c3db8a17a1a02300eaac7593cd7b707653db8a17aabb892641a02300eccab38bbe8484ae53db8a17acdbeb8aee6c09da267fe5c843db8a17a1a02300ece46ca963db8a17a4b61e89d4833a2b65d3c2283db8a17a97c7a940214c6c33db8a17af0906d68bd103ab91703253d30685a1c643a5b1b2e878d0a29e58051ccab38bbaad1cca149c2da41a02300ee1c291e3bd8cb0e2aac7593c7c91cb3ad2a2e19995275ed35f5d4ec8814087e31a02300e27f8ab2a1a02300e836a726b1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300eafbef10ec4d3411e1a02300e1a02300e3d5f6c413db8a17a1a02300e83d1b65344c2d4b838417b991a02300eaac7593c93298eff3db8a17acbd7c3c767fe5c84181bddbc1a02300e3db8a17a3db8a17ae75426013db8a17a349bd05d7d4e2019a255bece91f1e2dce136fb7391f1e2dc91f1e2dc5b3d5bda7d4e20197d4e2019ccab38bb1a02300e67fe5c84da4499587631ae9c3db8a17afaec4a6a44c2d4b81f4037dee2fe5dc1a02300e3e988c083db8a17a4fa9b5a0d86975521a02300ede0f8c383db8a17ab930c803381f185cb5ce7a543e988c0848f508a128683ea83db8a17ae23f299c1a02300ecb64b5f11fde3f3db8a17a149c2da4c5b9d5347d4e20191a02300e69ed2ac9b5db0a3a0cc5aaeb2f8d1c65c763af01a02300ee949b7531a02300e3db8a17a149c2da41a02300e1a02300e27a77001cdbeb8ae2ece737deb8b2e4b15628fb51a02300e700a6cabab698f6a3db8a17a3db8a17a3db8a17a3db8a17a3db8a17a5b40bf3f1a02300ed796a62a37dcdc481a02300e7d4e2019"

string5 = "906d681a02300ec4d3411e3a2bb5b39b86a8fa779467f03db8a17a215f4a879a3a3fd44499b54ebeaddd1ba0b27d262f2088d94ad314104c0a37223db8a17adf587e893db8a17a1a02300e3db8a17a3cb7e27a815587e22d553f33249cc55011b74e99dbc4a57317130de91a02300eaac7593c2188fd9b3db8a17ae1c125d656dded637f016490329a043b3db8a17a3db8a17a8ba38d7ddcf551b91a02300e7645fc0c6c90dad1fcbb0f86d1a79efa1a02300e1a02300e1a02300ef14a20e91a02300eadc1e02e530b02b1423dc1191a02300e1a02300e1a02300e1a02300e1a02300e7c91cb3acc8dea651a02300e3db8a17a12d8a2571a02300e1a02300e486a42f4257b4f1af8012d4512b27399c3598e95244808967e8859a8bd724ec4ecb84208291fe99a37c1dc87468d6707bb72af4b53dc554486a42f41a02300ede2fb7bd1a02300e1a02300e1a02300e1a02300e1a6758ab3db8a17a1a02300ecc8381d5c19ce261a02300eaac7593cdbc4a573244831133284eedb6d9615193b435b91a02300e4ac25a951a02300e9f2395e11a02300e1a02300e1a02300e774044d5e51ba0ff163e208386e51531a02300e8f3c41561a02300eab698f6a1a02300e2723a789cc0169401a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e1a02300e50854a934c0a537b3db8a17af253ab501a02300e1a02300ea65f1ca81a02300e11fde3f8640949d2bf2a59e21cede04977330a273e1fbc3db8a17a3db8a17a1a02300efd2e662ef72b5f4d1a02300ee180cb8d952a3cb41a02300e2cc07bca23300aca1a02300e2cc07bca1a02300ec19ce261aca8ca01a02300e3db8a17af55965d92ac76daaae4226adbcc166652bb755074aba7ac2ae4226adbcc16665415da6a04aba7ac21a02300e3db8a17a1a02300ed5a9ea7fe0b85a9fb930c8031a02300e3db8a17a6724ad69bbd6a2a23db8a17a11fde3f15ef62531a02300e1a02300e3db8a17a7303684a6d8878fd3d766f9facf6d79bad613d50c19ce2623a392af4ac25a95a2694ab2a40417c8ad2cde56c19ce2623a392af4ac25a95a2694ab2eb479b39731b25701a02300e1a02300e3db8a17a1a02300ee23c7f70823062346249a7c19910e4ea48a18ab1cb64b5f51d2a0131a02300efd388dcc1a02300ec4d3411e1a02300ec4d3411e1a02300ed4f034ab3db8a17a1d22e89aa66efd631d22e89acb8e9debede0edc11a02300eaac7593c3a50141ad30683cade67ca32e09d12922c68a55cd9b50800a0d8f605253a6128edca17c33838ba1d3e070f86b2a5610c974f9905a6ef7e447013e5281a02300e2723a7894018530aec87e1a654b5a1e01a02300e3db8a17a7b76f4aba0179129a3b150137d4e20197c7190b3254e95f253e4cd1d8df57d2038b6c8d2bbd6a2a2399fa633a57e700d3db8a17a11fde3f1a02300e1a02300e1a02300e4ce08803530b02b11a02300e7c91cb3a1a02300e3db8a17af2e397dd54cbac8646c01b36352b61431aa627d3d3711a41a2aab17bace1477af9b50c01a02300e252228babbd6a2a21a02300eccab38bb1a02300e3bca60efb641ffd57c8dee41a02300e3db8a17a1a02300e915b5386618dd0053db8a17a618dd0053db8a17a6343309b6343309b3db8a17a3db8a17a4c0a537b3db8a17a11fde3f11fde3fc821eb149124e43b81b91a55f30d1bda1a02300e57c44fab8905aff762b9746262b9746230b4d55130b4d55162127a6e62127a6e62127a6e62127a6e722887e21a02300e3db8a17a1a02300e3db8a17a4ac25a951a02300eccab38bb1a02300e57c44fab1a02300e7c91cb3a5b2db54c1a02300e7c91cb3a1d22e89ab7db6c9235e33bb9"

string6 = "50143030a82f03cdf057f15d7c91cb3a3db8a17a1a02300ea3f7793eb26c4d6fb41b302d64c7e5abd5be6f60751aefbfa20b859273f8242c4ef5a5cc07f970c36e80884f4960f674be6da91a02300e2a1ff6ed915b53863bbbac009e334cd73212a416653e3dea17ddcfd333a6f638dce3e4025d23cef67ee5bd4580b8162f25e1316724a623adede9ac90979444bb7d264a4753cc3c2c71a8cf9ab12c1aea95916357c91cb3a697d1ab8f239e0111a73f4eb14e2aff3c42077b6e65ad3c95b31556ac1607a9ec7268e232369ce13c37eb6aaa2400a67c9a258af752cbe29d7320c26342aadb8620365f7c91cb3af7613593a11b67de1a02300e7d4e201  9ac901105a0cc5aaede756804cc8aa01423b56494aac7593c500eee31c4d3411eb0a2979dbc81c416c21014d5c4d3411eee4ca402c7124379654498523db8a17aa52498c41a02300e1a40b0778e6d0310be82d0d99d1706271a02300e1a02300e1a02300e1a02300e94f7b8f11a02300edd4e44cd1a02300e6d9e40c3846fae4c7316d7461a02300e1a02300e"


# [c6d7]
# [ccab]
# [c]

# Function to tokenize a string into a set of characters
def tokenize_string(text):
    characters = []
    tokens = 2
    i = 0
    while i < len(text):
        characters.append((text[i:i+tokens]))
        i = i + tokens
    return set(characters)

# Tokenize the two strings
set1 = tokenize_string(string1)
set2 = tokenize_string(string2)

# Calculate Jaccard Similarity
intersection = len(set1.intersection(set2))
union = len(set1) + len(set2) - intersection
jaccard_similarity = intersection / union

# Calculate Jaccard Distance (1 - Jaccard Similarity)
jaccard_distance =  jaccard_similarity

# Print the results
#print("String 1:", set1)
#print("String 2:", set2)

levenshtein_distance = ratio(string1, string2)
jaro_distance = jaro_winkler(string1, string2)

print("Levenshtein is:", levenshtein_distance)
print("Jaccard Distance:", jaccard_distance)
print("Jaro Distance:", jaro_distance)
