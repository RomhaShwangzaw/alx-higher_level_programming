#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: The head of the list to be checked.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list->next;
	hare = list->next->next;

	while (hare)
	{
		if (tortoise == hare)
			return (1);

		tortoise = tortoise->next;
		hare = hare->next->next;
	}

	return (0);
}
