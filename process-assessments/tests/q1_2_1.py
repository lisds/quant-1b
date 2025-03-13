test = {
  'name': 'Question 1.2.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> genres = train_lyrics['Genre']
          >>> def check(r, k):
          ...     cls = classify(test_20.iloc[r], train_20, genres, k)
          ...     fds = fast_distances(test_20.iloc[r], train_20)
          ...     sorted_gs = genres[np.argsort(fds)[:k]]
          ...     vs, counts = np.unique(sorted_gs, return_counts=True)
          ...     return cls == vs[np.argsort(counts)[-1]]

          >>> check(0, 5)
          True
          >>> # Did you allow the function to use the input value for k?
          >>> check(0, 11)
          True
          >>> check(1, 5)
          True
          >>> check(1, 11)
          True
          >>> check(2, 5)
          True
          >>> check(2, 11)
          True
          >>> check(3, 5)
          True
          >>> check(3, 11)
          True
          >>> check(4, 5)
          True
          >>> check(4, 11)
          True
          >>> check(5, 5)
          True
          >>> check(5, 11)
          True
          >>> check(6, 5)
          True
          >>> check(6, 11)
          True
          >>> check(7, 5)
          True
          >>> check(7, 11)
          True
          >>> check(8, 5)
          True
          >>> check(8, 11)
          True
          >>> check(9, 5)
          True
          >>> check(9, 11)
          True
          >>> check(10, 5)
          True
          >>> check(10, 11)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
