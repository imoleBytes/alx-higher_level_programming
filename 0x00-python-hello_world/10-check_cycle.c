#include "lists.h"

/**
* check_cycle - this func check list cycle
* @list: pointer to the head of the list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *curr;
	listint_t *other;

	if (list == NULL || list->next == NULL)
		return (0);

	curr = list;
	other = list;

	while (curr != NULL && other != NULL && other->next != NULL)
	{
		curr = curr->next;
		other = other->next->next;

		if (curr == other)
			return (1);
	}
	return (0);
}
