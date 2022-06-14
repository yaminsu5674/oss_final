# oss_final

# How to build image
Download Dockerfile and go to the directory which includes Dockefile you downloaded just before.
And type below with tag_name you want.
```bash
docker build -t ANY_TAG .
```

# How to run Docker Container
And type below for running Container
```bash
docker run -d -p 8080:8080 ANY_TAG:latest
```

# Use Program
You can freely use this buyers and products program.

Do not paste all below commands, just type seeing this.

If you want to check "buyers" and "products" , You can choose below.
 
```bash
curl -X GET “http://localhost:8080/buyers”
curl -X GET “http://localhost:8080/products”
```

If you want to add "buyers" and "products" , You can choose below.
```bash
curl -X POST “http://localhost:8080/buyers?name=BUYER_NAME”
curl -X POST “http://localhost:8080/products?name=PRODUCT_NAME”
```

Any buyer can purchase any products . at once . for several times.
```bash
curl -X POST “http://localhost:8080/buyers/{BUYER_NAME}?prod_name={PRODUCT_NAME}”
```

If you want to get any buyer's purchased record. Type below.
```bash
curl -X GET “http://localhost:8080/buyers/BUYER_NAME/purchased”
```
