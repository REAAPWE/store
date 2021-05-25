from requests import get, post
import re
#By Team PT??.
print(get('http://artii.herokuapp.com/make?text=Team PT').text)
req = get("https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LftusIUAAAAAOW32HKzUJ89iC6hwjDmSRh1NABU&co=aHR0cHM6Ly9pZ3Rvci5jb206NDQz&hl=en&v=eWmgPeIYKJsH2R2FrgakEIkq&size=invisible&cb=t2x2im473ede").text
q = req.split('recaptcha-token" value="')[1]
name = q.split('">')[0]
data = {
		"v": "eWmgPeIYKJsH2R2FrgakEIkq",
		"reason": "q",
		"c": name,
		"k": "6LftusIUAAAAAOW32HKzUJ89iC6hwjDmSRh1NABU",
		"co": "aHR0cHM6Ly9hY2NvdW50cy5wdWJnLmNvbTo0NDM.",
		"hl": "en",
		"size": "invisible",
		"chr": "%5B89%2C64%2C27%5D",
		"vh": 13599012192,
		"bg": "!LiigKAHIAAX6VNIG-kcN_nIMK5YH2l1QXkVqQj_DwQcAAADtVwAAABJtAQecCt2dAvdad6qatov4PZ_tHbSWuPkYC4u0aGFwTOY7stoD-TvwvGGnZAE_RaHEdeS85c8BfI2znMdoVgw5RewIjN0tKnEwgV9zgVSUHAb0XHI08i95D7yuh0zcpSiTCPL5_nQHOSm7rTo_5LSlWyx0IiitfJVkTJ_4WJBMoVUjhTsagTxp2vsW_ELsNT1rQnzwW-wwyYRt-5L2iKZRtcQkcQ0tVmOgLnRpaAUD29_KL4vGS0pVN5FQursDmiWwsgaG-_d9b27lagSKIe8TpJZUBiCLwVifw_7JfU4-HBRmzvalpjUgxjWbiPnk4mwS532cioRaFUZ_jfOXELro-thRUC_50hSN1SoPwS_x3ihOJh2XVSrFXCLJH8wpaMN9w1yI9X0NAbPF4v0SaSlIumNznprsNFrkJoJyYLdRMucQEVWehNNKCZavWXDfydWoUq3u9WuQyrhQLc2OGOTbD7gG4ZC9i5_EPz6zQSksBDbMjDk95SwBO-ZkXdF47dPQfJQEsCLlY9vPPZMhcfSmYUFN11AWaicvcSc_isMbJgYuv7IN74l5ZySwrCik17h4SD0CJdf5M5D2RTxyBIVFd5oiFe3xIG-yl3MvxwGP19wl65UoaLhqZ_sd5r7OMsJhVlGc0Sb1SLUTK2a0rKXQfrTxwHwZYb3aUl76h3bFaEwayzI9dKSsBNAKhT_MYWeYd51V0JLMx70gtoa7D75phzfrlzyi6q2vfqwFRj6PLLEwucYtcvcOC1BuQmUPjKIihAu-cgZgR13BPdk4tMqUOEB7M_Ghf68Ce53wVzkrmUDH9aJ2aFiz-jLPMX6Plca3ainfQruTHB-pRz-35-fhQNBP-wspuEgFhkPAUIZLV3pStjZ7Fn_iWr1jRwcv1TgGOFXmBeTSCDucHkJqAyUm24ARchHDPGOrQ0rmTL6FPqaI7mHbFu2HoZPxfrrDRrU0cuqblknQFtiip4QZlYt7gQYBlT-wBUFX395Cish0cjeUQus5qBHMxJzSceYn7IPu94tOjXb0WbOaHD75htM5qBCuFxXAyYekM-nfnhd-m1XCiMr-32KxkdJBqWHDKCk6VXLJQKTutNghEYe35U_y9UjUdU8Q4d1wv7yi3-bWfEJqG4lQpQ9-nN6xUhkqqQdLAIU_i7rZMF2BspwdDly3iT7XF6RfQvE86HTU4fSG1jEmWOQ7dNTtv3WbOYZAHOpOf8KzOzQpMKQxXPl5ihIq2IRci-l-Gw2xoCRnvqV13VTK-VyBVYvIs9uSdCFq8pJ9c5M32bFcKe7ynKKKYKuC41qj5blutmolhHtzo74o1KoPEJcfDd3W70r3nPcIMEzYp6BY8JR-SJpuZwgzZMncBBmU517xfj8dvSYI0sFMGvRkgF7WKgHC8TL5AsO4XUi4UDaMree3cxNhXfwSztpLnrfhe3zgNH8M7spj4kcFmfpl4aiOVBkmlERybjHI2eVY19UVzr_CXMEDHiSURO5r5ryW5AW0_ZTbWvYG2hbhUbQieRAUteEAqCxJWCJhAoSce3PrsEBtBEPYwBdl9PNjjKlVXdKqYO_FxI4tyKgwXWOQ0YtbTn2Z4YDT9SjiCDCrGZBQNoQdf840vwTYgfqZMcsLG7lEutIn8haeEN2MBk8yQp_856Nb27-oQbdZdv2M9imDkulauQ_SVKxSCGA9Vvau5AnGhkeSu8Hy35I7y40QGUB2aLNPx_Wxk9dbyicbfjxsrHIZ_ez66ZBKvtWfpRug4LJ7R2dKQSdj-WHA_pAJIjGsu-mgZJp0B-wGccbmJsXsxanSlSXxophYFzXLVS-IqX7BDRLsy4y481kRtkq8ME_hzoxvLvNEd_XQ2-9k6vH1rT9MLdVcbaBacfiT3IjFQoM0KDCaM5M-js3yv-k_epTBbrMgceeEh8lrGBRvC7Et8dtboyUnpqNtODrzLfwQXGvkAxJyP9BmA_VcPI50zBLKdQJVAGrgD-IZf77cHK07CydeIbpGFg7co-Jb4qFJlzF1WgUWHM9nwgYUn3GASJf5spyfFlAUfic33EnCACD1c0YvXPPooGqK64MxTAZ5sEklkHp8U2WQU8Nf_VCJ9krC9_UGhJIo7aHz3Qk1TV-G-qOTfdzxkMNqc1lAmTOMfHSLcn6L3T86CYCmWelK4p4uXGK6A6ULPS_cPMz5MXlAoKlpAoA50uA0L_DKxgBreRdyCtKVt-vBzcIif5qTZ42vWpEh10BxlANoPBI8jDM0xcIp6lfklFsTHABQT9e-gDm0Np_ArsXVW_EPOvAqiN14u6BbEOIH-rHMyMa9SP9rhnPnKkqPXZ53H24EF429mTq_zYjejkj6uXvCf_v3XehPBNR1dMsSq2BCWMlkiK6EauTUrihfp93FjRxjzLIesqhjw2lH8cjBKyl2aM8rt2FJYPq_RpHpVv_-bEPny2DyTetFu7UZWQP6CFUkhVGIpt7x6iixvOsysWYTjfQ0SwhifET2-ls6XZJcH3CrYTNU94JU6wkkkJI1pMD2t0LZtbpTADmZRKNrZLcro5X1ciQ0rG0S_hSLXECv-5rIry3OkxZOW1TdAQmdFUHD4blq3kRXjvsko8qECENFYsL7uYyRxjd3SyAf3V8iSsvI8UbmSo-qWOa7YJk2_8WIp5HCaZNsjXpZycEDZvNwERS-J4N6sYQSyqoPNCh3GrOcodunV8MtDm9TbU41OJ3-6IxoSD--AAATm5ZhNEDdalW33kC0BfwL6n28-HhhluO43aOrHXDQZUiODsWIx4unZKgwl_L3cxHEoPIyOIreSk8i0WtkINL8ks0o7gNlDjaSsz7YoI9RdO9B-FcUDXAn51Yu0pL3nrpcaD7yOn3aBndoponcB0X28vJE0rvAQ8T1h4di1BFviipTS_gLjH6hJPQH8eWo_I8Xkr7k5CdZpNPq3OpDIBtB3LxIROFRqlfTf1elMbP5eNM2Mo4p6GiGubVNnbLAsEWpF8GuoP82MnD5GCYU82PM9GrJXilbYvAbKrPPDLTz76ccEQ5eYiD1xn2DKLo3couOWVAmzyrn_OKgkxGfwz2gy8hcTCDnPjOEVAXuDHH0tFIUUa0XCcnA-G84FMnGnZpU67wqGDO08WJOChsOq-k5Z5sh-VWioMOEl4VCUk-SvKXmQs-TLrrQZjD0sVH8B6iUTUzQ2Z97TQP2EYth--SfiiwXvWWihB98d4vM3aINUzIP5HIfFpZQygMhBPpKgtyzihfkdDJ-KC3wB3DctNOyYUo6Lc_D97uRufLObF6aL7lqQeZcRzgUr3Q7g5Wr_qpLf2bgyLCb-u9cEWA3PX6SWhr_0CcOWUk8d1PuC1oDy_sGAgEjFC0jd2-sYDFG1_wzXOELHBOG5NTK4sH9dfgwCq9vdMS-BIxLXQSrKxuZn9QSZGy0XN2jX9Db4m6oOGRISjwOVh8eaBvh-RGrjOsAy-aghS1NJhH5Sw6g1RM2C2nq4dPz5A5PjIMAKAbCIML17Axr3pHJkNSDXSUQrY6f9-xWF7QxjXod-6kWqjBpXbaOxlT5ORVNFu79sWtx3566FNpxfONLXH9zxV-V4m62Frq_4v2auhJPvkrXL_W6vnXcY6oyfxMWFcThagG4VdQlzBtHDYIuqyNco0Tr5SOONeCFvU27WQXWRMJIqI5pIiU1HwkIS_hX0X8zpBFt7FP1VsqnJETdxU_I1ThmbJjuwn91lN_HtillUFtJrTLoxvU0vIc"
}
req = post('https://www.google.com/recaptcha/api2/reload?k=6LftusIUAAAAAOW32HKzUJ89iC6hwjDmSRh1NABU', data=data).text
Captcha = re.compile('rresp","(.*?)"').search(req)[1]
headers = {
	"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
	"x-requested-with": "XMLHttpRequest"
}
req = get("https://igtor.com/robotVerify.php?yonlendir=https://igtor.com/", headers=headers).text
Link = input('[-] Link Video : ')
if 'reel' in Link:
	V = Link.split('/reel/')[1]
	Code = V.split('/')[0]
else:
	V = Link.split('/p/')[1]
	Code = V.split('/')[0]
data = {
	"mediaCode": Code,
	"recaptchaToken": Captcha,
	"miktar": "15"
}
req = post('https://igtor.com/inc/izlenme', headers=headers, data=data).text
if 'success' in req:
	print('[-] Done Send 15 Views')
else:
	print('[-] Please Wait 10 Min Or 600 Secend')