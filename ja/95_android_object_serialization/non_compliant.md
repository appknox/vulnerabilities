
安全でないコードの例 :

    bundle.putSerializable("exampleClass", exampleOfSerializabledClass);
    exampleOfSerializabledClass = bundle.getSerializable("exampleClass");

