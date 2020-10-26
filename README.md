# Prefect tutorials

## 1. Environment installation

If you have an old version of conda, you can use the following command to update your conda 

```bash
conda update -n base -c defaults conda
```

Now, you can create a virtual env with name prefect\(you can change it to whatever you want\), python 3.8

```bash
conda create -n prefect python=3.8
```

Activate your conda virtual env

```bash
conda activate prefect
```

{% hint style="success" %}
You should see your terminal change to the following form

\(prefect\) jovyan@3a8b3571afe2:~$ 
{% endhint %}

## 2. Install prefect

```bash
(prefect) jovyan@3a8b3571afe2:~$ pip install prefect
```

## 3. Create a new kernel with your conda virtual env 

Install ipython kernel 

```bash
pip install ipykernel
```

{% hint style="info" %}


```bash
(prefect) jovyan@3a8b3571afe2:~$ pip install ipykernel
```
{% endhint %}

Load your conda virtual env to your ipykernel 

```bash
python -m ipykernel install --user --name=prefect
```

If everything goes fine, you should see the following return text, and in your jupyter you will find a new kernel prefect

{% hint style="info" %}
Installed kernelspec prefect in /home/jovyan/.local/share/jupyter/kernels/prefect
{% endhint %}



## 4. Start a new notebook and choose prefect as kernel

