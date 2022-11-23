async function create_ix_tree() {
  await window.customElements.whenDefined('ix-tree');
  const tree = document.getElementById('tree');
  tree.model = {
    root: {
      id: 'root',
      data: null,
      hasChildren: true,
      children: ['sample'],
    },
    sample: {
      id: 'sample',
      data: {
        name: 'Sample',
      },
      hasChildren: true,
      children: ['sample-child-1', 'sample-child-2'],
    },
    'sample-child-1': {
      id: 'sample-child-1',
      data: {
        name: 'Sample Child 1',
      },
      hasChildren: false,
      children: [],
    },
    'sample-child-2': {
      id: 'sample-child-2',
      data: {
        name: 'Sample Child 2',
      },
      hasChildren: false,
      children: [],
    },
  };
}

(function () {
  import('https://cdn.jsdelivr.net/npm/@siemens/ix@1.1.0/loader/index.js')
    .then( module => module.defineCustomElements() )
    .then( unused => create_ix_tree() ) ;
})();
