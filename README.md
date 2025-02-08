# 🛡️ Hiding Python Source Code with Dill  

This repo shows how to hide Python source code while keeping its functionality using `dill`. The trick: serialize (`pickle`) a class, then delete or rename the original script—users can still use the class but can't extract its code!  

## 🚀 How It Works  

1️⃣ **Run `dill_source.py`** → Saves `MyClass` to `my_object.pkl`.  
2️⃣ **Rename/Delete `dill_source.py`**.  
3️⃣ **Run `dill_usage.py`** → Uses `MyClass` but can't retrieve its source!  

## 📌 Usage  

```sh
python dill_source.py  # Pickle the class
python dill_usage.py   # Try using it without the source
```

✅ The class still works.  
❌ The source code is hidden!  

## 📦 Dependencies  

Install required libraries:  
```sh
pip install dill numpy
```  

⚠️ **Note:** This method hides code but isn't foolproof against advanced reverse engineering.  

Happy coding! 🎉
