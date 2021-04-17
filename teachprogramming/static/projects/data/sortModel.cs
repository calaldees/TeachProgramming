using System.Collections.Generic;

public interface SortModelListener<T> {
    void displayState(AbstractSortModel<T> model);
    //void waitForInput();
}

public abstract class AbstractSortModel<T> {

    private List<SortModelListener<T>> listeners = new List<SortModelListener<T>>();

    protected T[] _data;
    protected List<int> _highlights = new List<int>();
    protected List<IndexPair> _pairs = new List<IndexPair>();

    protected uint _swaps = 0;
    protected uint _comparisons = 0;

    public AbstractSortModel(T[] data) {
        this._data = data;
    }

    public void addListener(SortModelListener<T> listener) {listeners.Add(listener);}
    public void removeListener(SortModelListener<T> listener) {listeners.Remove(listener);}

    public IEnumerable<T> items {
        get {foreach (T item in this._data) {yield return item;}}
    }

    T get(int index) {return this._data[index];}

    public int size {
        get {return this._data.Length;}
    }
    public int[] highlights {
        get {return this._highlights.ToArray();}
    }
    public IndexPair[] pairs {
        get {return this._pairs.ToArray();}
    }

    void clear() {
        this._highlights.Clear();
        this._pairs.Clear();
    }

    public void displayState() {
        foreach (SortModelListener<T> listener in this.listeners) {
            listener.displayState(this);
        }
    }

}

public /*data*/ class IndexPair {
    //public int a { get; init; }
    //public int b { get; init; }
    public int a;
    public int b;
    public IndexPair(int a, int b) {
        this.a = a;
        this.b = b;
    }
}