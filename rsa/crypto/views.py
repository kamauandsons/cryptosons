from django.shortcuts import render,redirect
from .forms import *
from .gen import *
from django.utils import six
from .pken import *
from .models import *

# Create your views here.

def index(request):
	return render(request,'index.html',{})

def signup(request):
    if request.method == 'POST':
        form = form1(request.POST)       
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()        
            return redirect('/')
    else:
        form = form1()
    return render(request, 'signup.html', {'form': form})

def key(request):
    y=0
    z=0
    if request.method=='POST':
        if 'gen' in request.POST:
            x=generateKey(1024)
            y=x[0]
            z=x[1]
    return render(request,'gen.html',{'pb':y,'pr':z})
def meso(request):
    if request.method=='POST':
        form=meso1(request.POST)
        if 'enc' in request.POST:
            a=request.POST
            t=dict(six.iterlists(a))
            p=list(t.values())[1][0]
            w=list(t.values())[2][0]    
            u=user.objects.filter(id=int(p)).values('public_key')
            z=u[0]    
            c=z.get("public_key","")       
            def readpubKeyFile():
                content2=list(map(int,c.strip().split(',')))
                keySize, n, EorD = content2[0],content2[1],content2[2]
                return (int(keySize), int(n), int(EorD))
            def encryptAndWriteToFile(message,blockSize=None):
                keySize, n, e = readpubKeyFile()
                if blockSize == None:
                    blockSize = int(math.log(2 ** keySize, len(SYMBOLS)))
                if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
                    sys.exit('ERROR: Block size is too large for the key and symbolset size. Did you specify the correct key file and encryptedfile?')
                encryptedBlocks = encryptMessage(message, (n, e), blockSize)
                for i in range(len(encryptedBlocks)):
                    encryptedBlocks[i] = str(encryptedBlocks[i])
                encryptedContent = ','.join(encryptedBlocks)
                encryptedContent = '%s_%s_%s' % (len(message), blockSize,encryptedContent)
                return encryptedContent               
        if form.is_valid():
            Meso=form.save()
            Meso.Message=encryptAndWriteToFile(w)
            Meso.save()         
            return redirect('/')
    else:
        form = meso1()
    return render(request,'message.html',{'form':form})
def dec(request):
    mess=Meso.objects.all()
    if request.method=='POST':
        r=request.POST
        tw=dict(six.iterlists(r))
        em=list(tw.values())[1][0]
        pk=list(tw.values())[2][0]  
        print(em)
        print(pk)
        def readpriKeyFile():
                content1=list(map(int,pk.strip().split(',')))
                keySize, n, EorD = content1[0],content1[1],content1[2]
                return (int(keySize), int(n), int(EorD))
        def readFromFileAndDecrypt(message2):
            keySize, n, d = readpriKeyFile()
            messageLength, blockSize, encryptedMessage = message2.split('_')
            messageLength = int(messageLength)
            blockSize = int(blockSize)
            if not (math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
                sys.exit('ERROR: Block size is too large for the key and symbolset size. Did you specify the correct key file and encryptedfile?')
            encryptedBlocks = []
            for block in encryptedMessage.split(','):
                encryptedBlocks.append(int(block))
            return decryptMessage(encryptedBlocks, messageLength, (n, d),blockSize)
        tf=readFromFileAndDecrypt(em)
        
    return render(request,'dec.html',{"mess":mess,"tf":tf})
