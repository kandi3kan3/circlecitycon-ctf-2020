Money Money Money Money
=======================
Put your wallet away. Money won't buy you the answer to this one.

```
2Hr6TcCiC1fauyi5ooQ5jQrTzeV7cfDzFSohGAYES1Xw63eEPyBU8Q3F1mhDDvfcp5fUejmzbtUBpfDBFvXsjwas8EehfUBsmJFPv7V4Hvw74H1EK3HruJS5GHeRrcgYxXEs4Zz4Th9K7H5xnAWiQp2P9YTybL72UvBukrQReSz8foRGgc1C1ppYEjYtMEikL
```

Writeup
-------
This one was a simple binary-to-text encoding.
I just opened up [CyberChef], which magically detected Base58 encoding:

```
"Mankind will discover objects in space sent to us by the watchers." ~ Nostradamus

CCC{SpaceMoney!Quasi_Universal_Intergalactic_Denomination}
```

CyberChef recipe:
https://gchq.github.io/CyberChef/#recipe=From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',false)&input=MkhyNlRjQ2lDMWZhdXlpNW9vUTVqUXJUemVWN2NmRHpGU29oR0FZRVMxWHc2M2VFUHlCVThRM0YxbWhERHZmY3A1ZlVlam16YnRVQnBmREJGdlhzandhczhFZWhmVUJzbUpGUHY3VjRIdnc3NEgxRUszSHJ1SlM1R0hlUnJjZ1l4WEVzNFp6NFRoOUs3SDV4bkFXaVFwMlA5WVR5Ykw3MlV2QnVrclFSZVN6OGZvUkdnYzFDMXBwWUVqWXRNRWlrTA

[CyberChef]: https://gchq.github.io/CyberChef/
