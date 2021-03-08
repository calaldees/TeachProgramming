using System;

class MainClass {

    public static void Main (string[] args) {new MainClass();}
    public MainClass() {
        string[] data = new string[]{"h", "b", "d", "g", "e", "c", "a", "f"};
        data = quickSort(data);
        Console.WriteLine(String.Join(",", data));
    }

    string[] bubbleSort(string[] data) {
        //Console.WriteLine("bubbleSort");
        bool has_changed = true;
        while (has_changed) {
            //Console.WriteLine(String.Join(",", data));
            has_changed = false;
            for (int i=0 ; i<data.Length-1 ; i++) {
                string a = data[i];
                string b = data[i+1];
                //Console.WriteLine("comparing "+i+":"+a+" with "+(i+1)+":"+b);
                if (string.Compare(a,b) > 0) {
                //Console.WriteLine("swap");
                data[i] = b;
                data[i+1] = a;
                has_changed = true;
                }
            }
        }
        return data;
    }


    string[] mergeSort(string[] data) {
        string[][] lists = new string[data.Length][];
        // Break every data item into it's own array
        for (int i=0 ; i<data.Length ; i++) {
            lists[i] = new string[]{data[i]};
        }
        for (int j=0 ; j<Math.Ceiling(lists.Length/2.0) ; j++) {
            //foreach (string[] ss in lists) {Console.WriteLine(String.Join("", ss == null ? new string[]{"null"} : ss));}
            int _j = IntPow(2,j+1);
            int __j = IntPow(2,j);
            for (int i=0 ; i<lists.Length ; i+=_j) {
                //Console.WriteLine($"i:{i} _j:{_j} __j:{__j} i+__j:{i+__j}");
                if (i+__j >= lists.Length) {continue;}
                lists[i] = mergeSortedLists(lists[i], lists[i+__j]);
                lists[i+__j] = null;
                //Console.WriteLine("yee");
            }
        }
        //Console.WriteLine("Done");
        return lists[0];
    }
    string[] mergeSortedLists(string[] aa, string[] bb) {
        //Console.WriteLine($"mergeSortedLists {String.Join("", aa)} {String.Join("", bb)}");
        string[] cc = new string[aa.Length + bb.Length];
        int ia = 0;
        int ib = 0;
        int ic = 0;
        while (ia<aa.Length || ib<bb.Length) {
            string va = ia<aa.Length ? aa[ia] : null;
            string vb = ib<bb.Length ? bb[ib] : null;
            //Console.WriteLine($"aa={ia}/{aa.Length} bb={ib}/{bb.Length} cc={ic}/{cc.Length} {String.Join("", aa)} {String.Join("", bb)} {String.Join("", cc)} va:{va} vb:{vb} va^vb:{String.Compare(va, vb)} va^vb:{String.Compare(vb, va)}");
            if (vb == null || va !=null && String.Compare(va, vb) == -1) {
                //Console.WriteLine("aa inc");
                cc[ic] = va;
                ia++;
            }
            if (va == null || vb !=null && String.Compare(va, vb) == 1) {
                //Console.WriteLine("bb inc");
                cc[ic] = vb;
                ib++;
            }
            ic++;
        }
        //Console.WriteLine($"done {String.Join("", cc)}");
        return cc;
    }
    public static int IntPow(int x, int pow) {return (int)Math.Pow(x, pow);}


    string[] quickSort(string[] data) {
        return quickSort(data, 0, data.Length-1);
    }
    string[] quickSort(string[] data, int lo, int hi) {
        if (lo >= hi) {return data;}
        int p = quickSortPartition(data, lo, hi);
        quickSort(data, lo, p);
        quickSort(data, p+1, hi);
        return data;
    }
    int quickSortPartition(string[] data, int lo, int hi) {
        string pivot = data[(lo+hi)/2];
        while (true) {
            while (String.Compare(data[lo], pivot) == -1) {lo++;}
            while (String.Compare(data[hi], pivot) == 1) {hi--;}
            if (lo>=hi) {return hi;}
            string v_lo = data[lo];
            string v_hi = data[hi];
            data[lo] = v_hi;
            data[hi] = v_lo;
        }
    }

}
