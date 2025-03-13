test = {
  'name': 'Question 1.1.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> list(genre_and_distances) == ['Genre', 'Distance']
          True
          >>> len(genre_and_distances) == len(train_lyrics)
          True
          >>> print(genre_and_distances.groupby('Genre').count())
                   Distance
          Genre            
          Country       596
          Hip-hop       587
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(genre_and_distances['Distance'],
          ...             sorted(fast_distances(test_20.iloc[0], train_20)))
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
