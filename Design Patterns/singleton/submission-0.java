static class Singleton {

    private static Singleton singleInstance = null;
    private String value = null;
    private Singleton() {}

    public static Singleton getInstance() {

        if (singleInstance == null){
            singleInstance = new Singleton();
        }

        return singleInstance;

    }

    public String getValue() {

        return value;

    }

    public void setValue(String value) {

        this.value = value;

    }
    
}
