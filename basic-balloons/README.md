Basic Balloons
==============
We found this message hidden on a computer. Please decode what it says:

```
EJHG65DINFXGOIDJNYQHI2DFEB3W64TMMQQGGYLOEBXW4ZJANFWWCZ3JNZSSAYTFMZXXEZLIMFXGILBANZXXIIDUNBSSA3DFMFZXIIDUNBUW4ZZMEBSXMZLSPF2GQ2LOM4QGS4ZANVQWIZJAOVYCA33GEBZW6IDNMFXHSIDVNZUXC5LFEBYGC4TUNFRXK3DBOJZSA5DIMF2CAY3BNZXG65BAMJSSAZTPOJZWKZLOFYRCA7RAJZXXG5DSMFSGC3LVOMFEGQ2DPNKHEZLFK5UXUYLSMQQU6TKHFVEXIJ3TL5QW433UNBSXEX3CMFWGY33PNZ6QU2DUORYHGORPF53XO5ZOPFXXK5DVMJSS4Y3PNUXXOYLUMNUD65R5GRKDQ3LYOFJEI4BUO4======
```

Writeup
-------
This one was a simple binary-to-text encoding.
I just opened up [CyberChef], which magically detected Base32 encoding:

```
"Nothing in the world can one imagine beforehand, not the least thing, everything is made up of so many unique particulars that cannot be forseen." ~ Nostradamus

CCC{TreeWizard!OMG-It's_another_balloon}

https://www.youtube.com/watch?v=4T8mxqRDp4w
```

CyberChef recipe:
https://gchq.github.io/CyberChef/#recipe=From_Base32('A-Z2-7%3D',false)&input=RUpIRzY1RElORlhHT0lESk5ZUUhJMkRGRUIzVzY0VE1NUVFHR1lMT0VCWFc0WkpBTkZXV0NaM0pOWlNTQVlURk1aWFhFWkxJTUZYR0lMQkFOWlhYSUlEVU5CU1NBM0RGTUZaWElJRFVOQlVXNFpaTUVCU1hNWkxTUEYyR1EyTE9NNFFHUzRaQU5WUVdJWkpBT1ZZQ0EzM0dFQlpXNklETk1GWEhTSURWTlpVWEM1TEZFQllHQzRUVU5GUlhLM0RCT0paU0E1RElNRjJDQVkzQk5aWEc2NUJBTUpTU0FaVFBPSlpXS1pMT0ZZUkNBN1JBSlpYWEc1RFNNRlNHQzNMVk9NRkVHUTJEUE5LSEVaTEZLNVVYVVlMU01RUVU2VEtIRlZFWElKM1RMNVFXNDMzVU5CU1hFWDNDTUZXR1kzM1BOWjZRVTJEVU9SWUhHT1JQRjUzWE81Wk9QRlhYSzVEVk1KU1M0WTNQTlVYWE9ZTFVNTlVENjVSNUdSS0RRM0xZT0ZKRUk0QlVPND09PT09PQ

[CyberChef]: https://gchq.github.io/CyberChef/
