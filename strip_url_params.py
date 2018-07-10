# Written by: Cameron Napoli

# Python code to strip repetitive URL Parameters

def strip_url_params(url, params_to_strip = []):
    pos = url.find("?")
    if pos != -1 :
        urlParams = url[pos:][1:].split("&")
        paramDict = {}
        keyOrder = [] # key stack to preserve order
        for param_pair in urlParams:
            splitP = param_pair.split("=");
            if not (splitP[0] in keyOrder) and not (splitP[0] in params_to_strip): # splitP[0] is the parameter name
                paramDict[splitP[0]] = splitP[1]
                keyOrder.append(splitP[0])
        # Now reconstruct the parameters in the same order
        reconstructedParams = "";
        for key in keyOrder:
            reconstructedParams += str(key) +"="+ str(paramDict[key]) + "&"
        return url[:pos] + "?" + reconstructedParams[:-1]
    else:
        return url


print(strip_url_params('www.codewars.com?a=1&b=2&a=2')) # returns 'www.codewars.com?a=1&b=2'
print(strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b'])) # returns 'www.codewars.com?a=1'
print(strip_url_params('www.codewars.com', ['b'])) # returns 'www.codewars.com'
