"""DEX Pairs configuration"""

# pylint: disable = C0302
# fmt: off

DEX_PAIRS = [
  {
    "name": "ADA-DJED",
    "token1_policy": "",
    "token1_name": "lovelace",
    "token1_decimals": 6,
    "token2_policy": "8db269c3ec630e06ae29f74bc39edd1f87c819f1056206e879a1cd61",
    "token2_name": "446a65644d6963726f555344",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "d944eda9d4fd8c26171a4362539bfd4ccf35f5a4d0cc7525b22327b997a4f4b9"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwap",
        "address": "addr1w9qzpelu9hn45pefc0xr4ac4kdxeswq7pndul2vuj59u8tqaxdznu",
        "security_token_policy": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "security_token_name": "7020f803"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1x8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz26rnxqnmtv3hdu2t6chcfhl2zzjh36a87nmd6dwsu3jenqsslnz7e",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de14073d8b3fb8109a7d573662f5967eb49f35635635682bfe8faae3f901a"
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnayvrzwt47mccrc8akjdnwat82r82man0g3s2m9czqdja6mfsqmv4gp",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhq6d77rk0jjxny493quf2pv32xup2ucx6hp6enfjg8gnjq0qqzlqam",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "ADA-USDA",
    "token1_policy": "",
    "token1_name": "lovelace",
    "token1_decimals": 6,
    "token2_policy": "fe7c786ab321f41c654ef6c1af7b3250a613c24e4213e0425a7ae456",
    "token2_name": "55534441",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1x8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz26rnxqnmtv3hdu2t6chcfhl2zzjh36a87nmd6dwsu3jenqsslnz7e",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de140c6ad22f3f52ddd285876d67a7357d7cf25ee10fe942f3547e371bcd6"
      },
      {
        "source": "VyFi",
        "address": "addr1z955fyznplf6hnuf4tgzwkpjqwe8x5yq7n5yrehp3xkypm9ksyd8pn7amnr48geat0yft0uezfunealzy4ghl0cayp4snfzxkj",
        "security_token_policy": "f7f9777979a2a96777823f149e6696954f43967fc56cfc7095a33f98",
        "security_token_name": ""
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhqc5jq5npz5xdnmdzjh7ez6e4j5xst29eqgcnmzyf60zmadsq3q9h0",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "ADA-USDM",
    "token1_policy": "",
    "token1_name": "lovelace",
    "token1_decimals": 6,
    "token2_policy": "c48cbb3d5e57ed56e276bc45f99ab39abe94e6cd7ac39fb402da47ad",
    "token2_name": "0014df105553444d",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "116df62938bc100b55c0e72b57a48dced2f928635ad66660bc165a8f40f8e735"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "Splash",
        "address": "addr1x89ksjnfu7ys02tedvslc9g2wk90tu5qte0dt4dge60hdudj764lvrxdayh2ux30fl0ktuh27csgmpevdu89jlxppvrsg0g63z",
        "security_token_policy": "7a3b08bf74ac6283edf40087f4b53e9b01b0d46a59fee3dd417fda9d",
        "security_token_name": "0014df105553444d5f4144415f4e4654"
      },
      {
        "source": "SundaeSwap",
        "address": "addr1w9qzpelu9hn45pefc0xr4ac4kdxeswq7pndul2vuj59u8tqaxdznu",
        "security_token_policy": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "security_token_name": "70204f05"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de14064f35d26b237ad58e099041bc14c687ea7fdc58969d7d5b66e2540ef"
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnaytmskjm3nhaazcv20yhs07hel96yv29zuf0gzlk5dt9ugzs2y5pq5",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhqlm3e807762pklheldndtjhrk0qxzzfh9vhc9kkc706xglsv8s5nq",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "ADA-iUSD",
    "token1_policy": "",
    "token1_name": "lovelace",
    "token1_decimals": 6,
    "token2_policy": "f66d78b4a3cb3d37afa0ec36461e51ecbde00f26c8f0a68f94b69880",
    "token2_name": "69555344",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "8fde43a3f0b9f0e6f63bec7335e0b855c6b62a4dc51f1b762ccb6dfbbafcfe47"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de140c7ef237f227542a0c8930d37911491c56a341fdef8437e0f21d024f8"
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnaytpq3ryg76qvca5eu9c6py33ncg8zf09nh7gy2cvdps2yeqlvvkfh",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhq7nzm5jzjeevh40p5h3f682mv3r6fnnsldx749n52asr6vsnevx3j",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "BODEGA-ADA",
    "token1_policy": "5deab590a137066fef0e56f06ef1b830f21bc5d544661ba570bdd2ae",
    "token1_name": "424f44454741",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1x8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz26rnxqnmtv3hdu2t6chcfhl2zzjh36a87nmd6dwsu3jenqsslnz7e",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de14068184e9f85dbd65ed9cc1a3d4f519acc060bb95e0a8a2a5dd7998a87"
      }
    ]
  },
  {
    "name": "CBLP-ADA",
    "token1_policy": "ee0633e757fdd1423220f43688c74678abde1cead7ce265ba8a24fcd",
    "token1_name": "43424c50",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "dfe1be4e42a1cf6a8f5648e904bef0b4b11ee8ca4131521b5256856ef34e3486"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1x8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz26rnxqnmtv3hdu2t6chcfhl2zzjh36a87nmd6dwsu3jenqsslnz7e",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de140549bd196264a186d09e00bcfd41727622e515154612f76dc6b8120b9"
      }
    ]
  },
  {
    "name": "FACT-ADA",
    "token1_policy": "a3931691f5c4e65d01c429e473d0dd24c51afdb6daf88e632a6c1e51",
    "token1_name": "6f7263666178746f6b656e",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "b4ba2b47edce71234f328fa20efdb25c3f96e348ca19a683193880489bb368db"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwap",
        "address": "addr1w9qzpelu9hn45pefc0xr4ac4kdxeswq7pndul2vuj59u8tqaxdznu",
        "security_token_policy": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "security_token_name": "7020fb04"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de140a5b624b96af21138b6dff057e0499e7f767fcfe7ac8adb549f3818d7"
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnayg6pp9snyy9v7uwarxd7dqc5k52egtc49y5w5h3nqqdy6qs2nzs8y",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhqadav244fusrvfjcrdra646ude8dlctzmv6wvsqtndwrdfsvg56qt",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "FLDT-ADA",
    "token1_policy": "577f0b1342f8f8f4aed3388b80a8535812950c7a892495c0ecdf0f1e",
    "token1_name": "0014df10464c4454",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "bbfe2d3033ea40ed27733fc1ec30b8994d59cf28eed9268746ab41619960cae6"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de1401a1136d9c9b4ebe90445939d02301c940fc04c1f8b8eedef2e29e102"
      }
    ]
  },
  {
    "name": "HOSKY-ADA",
    "token1_policy": "a0028f350aaabe0545fdcb56b039bfb08e4bb4d8c4d7c3c7d481c235",
    "token1_name": "484f534b59",
    "token1_decimals": 0,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "11e236a5a8826f3f8fbc1114df918b945b0b5d8f9c74bd383f96a0ea14bffade"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwap",
        "address": "addr1w9qzpelu9hn45pefc0xr4ac4kdxeswq7pndul2vuj59u8tqaxdznu",
        "security_token_policy": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "security_token_name": "702011"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1x8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz26rnxqnmtv3hdu2t6chcfhl2zzjh36a87nmd6dwsu3jenqsslnz7e",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de140455422de9777d248aaaa71da9e17f67ddb6e003aadea1f4f97d24ddd"
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnayvgedqwg3tvxxvhlgnrzujmpw9qful70s6tfga5gyadds4qsksxeq",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhqahnnkdeex48glxptpj65zc5jyp7rhynd0fplm3sznpl7xsu9g7vd",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "IAG-ADA",
    "token1_policy": "5d16cc1a177b5d9ba9cfa9793b07e60f1fb70fea1f8aef064415d114",
    "token1_name": "494147",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "CSwap",
        "address": "addr1z8ke0c9p89rjfwmuh98jpt8ky74uy5mffjft3zlcld9h7ml3lmln3mwk0y3zsh3gs3dzqlwa9rjzrxawkwm4udw9axhs6fuu6e",
        "security_token_policy": "a00d48eff61d8cfd86b5795d0b15015b84a33f139f22e7c8e3005c34",
        "security_token_name": "63"
      },
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "bdfd144032f09ad980b8d205fef0737c2232b4e90a5d34cc814d0ef687052400"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de1406f79e3e55eef82b9d03cf62cc3d4a6d0d03b00bf7b1b43330f829779"
      },
      {
        "source": "VyFi",
        "address": "addr1z923yccpjgvf3lk2n3u4zl25vjm7227y5lswvyg2g6387z8qy02w7ayk0lyyrf080l5zusdpkg8se9x7fcke6vaz42lq7dg4ty",
        "security_token_policy": "91273656a81cc90ae6a5403a39052eeae71f17332cc1928be01ec656",
        "security_token_name": ""
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnayw3e26v9tyaqqvhqlzngl5afw2ls5j5se2z7msh30pz0vwsscveaf",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhq7lz3zuxz0l95ne0pwxdy0r7uvyqmx39l0nv4jyc9g59ngsj543je",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "INDY-ADA",
    "token1_policy": "533bb94a8850ee3ccbe483106489399112b74c905342cb1792a797a0",
    "token1_name": "494e4459",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "571cdbdfae07f098049b917007366cca8f2e0770a7b2bae5f7726f36849fbcb9"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwap",
        "address": "addr1w9qzpelu9hn45pefc0xr4ac4kdxeswq7pndul2vuj59u8tqaxdznu",
        "security_token_policy": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "security_token_name": "7020b003"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de14027f51c29cde11887b667d9632533677a82baa305a6ea43993b68909e"
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnayv4uuuctkmfnszaeqv30txrfxxzssrdsd20vv6afc8pgxfszanerm",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhqe8lgvywlrjje5skanlxz2h6dcyp6vzp6yt84aeafq8dsesrwpttn",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "LQ-ADA",
    "token1_policy": "da8c30857834c6ae7203935b89278c532b3995245295456f993e1d24",
    "token1_name": "4c51",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxzv3ypnc5g2ndrjke3lhpad6krx2r9d2ghrlguw9mv4453vqgekewd",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "1b7f4abbf3eb04f8a7e5fbbc2042c524210dd960b6703a02fe52f70a7701e284"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwap",
        "address": "addr1w9qzpelu9hn45pefc0xr4ac4kdxeswq7pndul2vuj59u8tqaxdznu",
        "security_token_policy": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "security_token_name": "702003"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de14019cd76d01ecb039aea8915a97e9186b0c2ce9ce56d041aece9862086"
      },
      {
        "source": "VyFi",
        "address": "addr1z8kkjw83qmz280rvqerqep7a7vgukxyfcxdh2xj0992frme8kq9dr3l47k6mfgvuugac48lc7p9zq25t6r4323hjux9qrzxrld",
        "security_token_policy": "60d04ebc9b110ba8690fe79204d23ad7e94f060221fa02d037126ffd",
        "security_token_name": ""
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnayg4pn8uxr87tguqw8jkn6p233rk7k683ppl2mspr8appw9q640ms8",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhq6pr0ayfupfkpyjs0lxpyulnd9wq4ct2zmaz0rg0e8zpjyq7wxle2",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "MIN-ADA",
    "token1_policy": "29d222ce763455e3d7a09a665ce554f00ac89d2e99a1a83d267170c6",
    "token1_name": "4d494e",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "6aa2153e1ae896a95539c9d62f76cedcdabdcdf144e564b8955f609d660cf6a2"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwap",
        "address": "addr1w9qzpelu9hn45pefc0xr4ac4kdxeswq7pndul2vuj59u8tqaxdznu",
        "security_token_policy": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "security_token_name": "702018"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de140129627c250a35b7db2e11f6b0e0370515ffa99452b549ef586753907"
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnaywr4j54yfgqvlgs3q9cz28m7aecmcg0walzm2mgmqar89ws34cp4w",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "PALM-ADA",
    "token1_policy": "b7c5cd554f3e83c8aa0900a0c9053284a5348244d23d0406c28eaf4d",
    "token1_name": "50414c4d0a",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhqmzknddfjp0x7ppfhqlxvksf7vacn2slgkv4pn095ycn7xsv4pm6y",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "REE-ADA",
    "token1_policy": "e7befada6a028d4bd20ae87edecf1ca04d65a1ff57b9f84f0d9847d2",
    "token1_name": "524545",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      }
    ]
  },
  {
    "name": "SHEN-ADA",
    "token1_policy": "8db269c3ec630e06ae29f74bc39edd1f87c819f1056206e879a1cd61",
    "token1_name": "5368656e4d6963726f555344",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "53225313968e796f2c1e0b57540a13c3b81e06e2ed2637ac1ea9b9f4e27e3dc4"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwap",
        "address": "addr1w9qzpelu9hn45pefc0xr4ac4kdxeswq7pndul2vuj59u8tqaxdznu",
        "security_token_policy": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "security_token_name": "7020f903"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1x8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz26rnxqnmtv3hdu2t6chcfhl2zzjh36a87nmd6dwsu3jenqsslnz7e",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de140eaab8141f57724a0ebce5525d0836fa574d385b0aa76c9102ab4fb0e"
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnayd8awyllkdhpwm7r3tnvvm0mzx592fzgazhuevl679cf7lq35qw53",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhql7dn3k9gsv72xxejmkazykmdq5ar9ppy9jgn24kgjfp36ql0yz56",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "SNEK-ADA",
    "token1_policy": "279c909f348e533da5808898f87f9a14bb2c3dfbbacccd631d927a3f",
    "token1_name": "534e454b",
    "token1_decimals": 0,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "CSwap",
        "address": "addr1z8ke0c9p89rjfwmuh98jpt8ky74uy5mffjft3zlcld9h7ml3lmln3mwk0y3zsh3gs3dzqlwa9rjzrxawkwm4udw9axhs6fuu6e",
        "security_token_policy": "8e50527b8cc1763348b393dca349bf04385ee12d4568afa0c8a457a9",
        "security_token_name": "63"
      },
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "63f2cbfa5bf8b68828839a2575c8c70f14a32f50ebbfa7c654043269793be896"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "Splash",
        "address": "addr1x89ksjnfu7ys02tedvslc9g2wk90tu5qte0dt4dge60hdudj764lvrxdayh2ux30fl0ktuh27csgmpevdu89jlxppvrsg0g63z",
        "security_token_policy": "ce1a4f1103fca3f93c1ba9b4e87fb0d9e855d66965ca3cf45165824a",
        "security_token_name": "534e454b5f4144415f4e4654"
      },
      {
        "source": "SundaeSwap",
        "address": "addr1w9qzpelu9hn45pefc0xr4ac4kdxeswq7pndul2vuj59u8tqaxdznu",
        "security_token_policy": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "security_token_name": "70201f04"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de140cacb7fd5f5b84bf876d40dc60d4991c72112d78d76132b1fb769e6ad"
      },
      {
        "source": "VyFi",
        "address": "addr1zy3jcyykdnjd3enu96hp0w6hct85s499w5y6w5hmk0qzh50qy02w7ayk0lyyrf080l5zusdpkg8se9x7fcke6vaz42lqwjjflq",
        "security_token_policy": "96c31772282e6ae5c629120471c5bbcdef538226b31b97d74c50ca3c",
        "security_token_name": ""
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnay2lz4g5wy95jwh2l6ca2jyq5xu8aga0fh3jyplef6m0npeslcq0pj",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhqlhhdq34c6wgm2u5xkg84nqkql6vq6fzm5grzcequr2rmwqwgf0zz",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "STRIKE-ADA",
    "token1_policy": "f13ac4d66b3ee19a6aa0f2a22298737bd907cc95121662fc971b5275",
    "token1_name": "535452494b45",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "CSwap",
        "address": "addr1z8ke0c9p89rjfwmuh98jpt8ky74uy5mffjft3zlcld9h7ml3lmln3mwk0y3zsh3gs3dzqlwa9rjzrxawkwm4udw9axhs6fuu6e",
        "security_token_policy": "83911d2a8db0a1c307f025c873359a3f2f0c580d5572e3c01f846f6f",
        "security_token_name": "63"
      },
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "9903ee543a02bb1743265ec0cda8da7e298d2dde14ae79f9fa6d0e28796cee88"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "Splash",
        "address": "addr1xxw7upjedpkr4wq839wf983jsnq3yg40l4cskzd7dy8eyndj764lvrxdayh2ux30fl0ktuh27csgmpevdu89jlxppvrsgddq74",
        "security_token_policy": "e73e65176c6bd31dbc878e317e852c826a534fb949d279a463ecbd18",
        "security_token_name": "535452494b455f4144415f4e4654"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1x8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz26rnxqnmtv3hdu2t6chcfhl2zzjh36a87nmd6dwsu3jenqsslnz7e",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de140e20b2a2ada3297878401938f077edfa329fa5706f0a046d15477650c"
      }
    ]
  },
  {
    "name": "SUNDAE-ADA",
    "token1_policy": "9a9693a9a37912a5097918f97918d15240c92ab729a0b7c4aa144d77",
    "token1_name": "53554e444145",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwap",
        "address": "addr1z8snz7c4974vzdpxu65ruphl3zjdvtxw8strf2c2tmqnxz2j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq0xmsha",
        "security_token_policy": "0be55d262b29f564998ff81efe21bdc0022621c12f15af08d0f2ddb1",
        "security_token_name": "9725d4168d06e85cc6bec7ab0e9bdd2b0120d880bb148ab21336774706eecdc8"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwap",
        "address": "addr1w9qzpelu9hn45pefc0xr4ac4kdxeswq7pndul2vuj59u8tqaxdznu",
        "security_token_policy": "0029cb7c88c7567b63d1a512c0ed626aa169688ec980730c0473b913",
        "security_token_name": "702008"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de1402f36866691fa75a9aab66dec99f7cc2d297ca09e34d9ce68cde04773"
      },
      {
        "source": "WingRiders",
        "address": "addr1z8nvjzjeydcn4atcd93aac8allvrpjn7pjr2qsweukpnay0sxtrcu2m27nn97yxpq50xc2xyrzggr409le9cytyvqgrsg55se7",
        "security_token_policy": "026a18d04a0c642759bb3d83b12e3344894e5c1c7b2aeb1a2113a570",
        "security_token_name": "4c"
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhqc99h387facw7t2k2nn2gvzvzl47hp7pena8dz3rgssdunsy5826s",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  },
  {
    "name": "SURF-ADA",
    "token1_policy": "2d9db8a89f074aa045eab177f23a3395f62ced8b53499a9e4ad46c80",
    "token1_name": "464c4f57",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "CSwap",
        "address": "addr1z8ke0c9p89rjfwmuh98jpt8ky74uy5mffjft3zlcld9h7ml3lmln3mwk0y3zsh3gs3dzqlwa9rjzrxawkwm4udw9axhs6fuu6e",
        "security_token_policy": "f7e8f4ce8c153b99acbcf201e18c67be2cacd4a0d812458d0d5834bc",
        "security_token_name": "63"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "Splash",
        "address": "addr1xxw7upjedpkr4wq839wf983jsnq3yg40l4cskzd7dy8eyndj764lvrxdayh2ux30fl0ktuh27csgmpevdu89jlxppvrsgddq74",
        "security_token_policy": "50e1fdf5cb92c367afb28445a2ba82c5be351f6300924799c032b5a5",
        "security_token_name": "464c4f575f4144415f4e4654"
      }
    ]
  },
  {
    "name": "SURGE-ADA",
    "token1_policy": "e992ef75f2367e6ecd93716ae88eba0d005dd91fd3a21f650b6496b5",
    "token1_name": "5355524745",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      }
    ]
  },
  {
    "name": "WMTX-ADA",
    "token1_policy": "e5a42a1a1d3d1da71b0449663c32798725888d2eb0843c4dabeca05a",
    "token1_name": "576f726c644d6f62696c65546f6b656e58",
    "token1_decimals": 6,
    "token2_policy": "",
    "token2_name": "lovelace",
    "token2_decimals": 6,
    "sources": [
      {
        "source": "CSwap",
        "address": "addr1z8ke0c9p89rjfwmuh98jpt8ky74uy5mffjft3zlcld9h7ml3lmln3mwk0y3zsh3gs3dzqlwa9rjzrxawkwm4udw9axhs6fuu6e",
        "security_token_policy": "c3c6686be48991209904f9652d9e6ba6e2c946429c5d68d0a3dd5792",
        "security_token_name": "63"
      },
      {
        "source": "MinSwapV2",
        "address": "addr1z84q0denmyep98ph3tmzwsmw0j7zau9ljmsqx6a4rvaau66j2c79gy9l76sdg0xwhd7r0c0kna0tycz4y5s6mlenh8pq777e2a",
        "security_token_policy": "f5808c2c990d86da54bfc97d89cee6efa20cd8461616359478d96b4c",
        "security_token_name": "4d5350"
      },
      {
        "source": "SundaeSwapV3",
        "address": "addr1z8srqftqemf0mjlukfszd97ljuxdp44r372txfcr75wrz2auzrlrz2kdd83wzt9u9n9qt2swgvhrmmn96k55nq6yuj4qw992w9",
        "security_token_policy": "e0302560ced2fdcbfcb2602697df970cd0d6a38f94b32703f51c312b",
        "security_token_name": "000de1403e259cc410c7932ff0f579085cb47e882498f1af51f1d8db90bc14fc"
      },
      {
        "source": "VyFi",
        "address": "addr1z9ts0u4xn7mcj073gxw64cw0xmz22apq7c8glvfeda7n8n9ksyd8pn7amnr48geat0yft0uezfunealzy4ghl0cayp4s3pksc5",
        "security_token_policy": "3b33dbef13ccf577299a7119f6d57cdef1514e5d488cbc2a44d9c17a",
        "security_token_name": ""
      },
      {
        "source": "WingRidersV2",
        "address": "addr1zxhew7fmsup08qvhdnkg8ccra88pw7q5trrncja3dlszhq6yhy84nmzwpx44rdpasg39q22a8mvev57h8r394pjst5mqnyxs4e",
        "security_token_policy": "6fdc63a1d71dc2c65502b79baae7fb543185702b12c3c5fb639ed737",
        "security_token_name": "4c"
      }
    ]
  }
]
