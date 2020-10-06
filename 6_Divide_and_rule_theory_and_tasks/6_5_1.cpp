// Задача на программирование: точки и отрезки

#include <vector>
#include <set>
#include <algorithm>
#include <numeric>
#include <iostream>

int main()
{
  unsigned n, m;
  std::cin >> n >> m;

  using Segment = std::pair<int, int>;
  std::vector<Segment> segments(n);
  for (Segment &segment : segments)
    std::cin >> segment.first >> segment.second;

  std::vector<int> points(m);
  std::vector<unsigned> counts(m);
  for (int &point : points)
    std::cin >> point;

  // Сортируем отрезки по началам
  std::sort(segments.begin(), segments.end());

  // Сортируем точки (через индексный массив)
  std::vector<unsigned> point_index(m);
  std::iota(point_index.begin(), point_index.end(), 0u);
  std::sort(point_index.begin(), point_index.end(), 
    [&](unsigned li, unsigned ri) { return points[li] < points[ri]; });

  // Заводим список активных отрезков - упорядочен по концам отрезков
  auto cmp_second = 
    [](const Segment *lhs, const Segment *rhs) { return lhs->second < rhs->second; };
  std::multiset<const Segment *, decltype(cmp_second)> active_segments(cmp_second);
  // Изначально этот список пуст

  auto it_segment = segments.begin();
  for (unsigned i_point : point_index)
  {
    // Очередная точка
    int point = points[i_point];

    // Поддерживаем список активных отрезков
    // Удаляем уходящие отрезки ...
    while (!active_segments.empty() && (*active_segments.begin())->second < point)
      active_segments.erase(active_segments.begin());

    // ... и добавляем приходящие отрезки
    for (; it_segment != segments.end() && it_segment->first <= point; ++it_segment)
      if (it_segment->second >= point)
        active_segments.insert(&*it_segment);

    // Ответ для текущей точки - количество активных отрезков
    counts[i_point] = active_segments.size();
  }

  for (unsigned count : counts)
    std::cout << count << " ";

  std::cout << std::endl;
}